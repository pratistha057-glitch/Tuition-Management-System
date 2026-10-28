from decimal import Decimal, InvalidOperation

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from apps.fees.models import FeesModel
from apps.payments.models import PaymentModel, Status


def process_khalti_payment(request, fee_id):
    if request.method != "POST":
        return redirect("fee-list")

    fee = get_object_or_404(FeesModel, pk=fee_id)

    try:
        paid_amount = Decimal(request.POST.get("amount", "0"))
    except (InvalidOperation, TypeError):
        return HttpResponse("Invalid amount format.", status=400)

    # Payment amount must be greater than zero.
    if not paid_amount.is_finite() or paid_amount <= 0:
        return HttpResponse(
            "Amount must be greater than zero.",
            status=400,
        )

    # Payment cannot exceed the remaining fee balance.
    if paid_amount > fee.remaining_amount:
        return HttpResponse(
            f"Cannot pay more than the remaining balance "
            f"(Rs. {fee.remaining_amount}).",
            status=400,
        )

    # Check whether the Khalti secret key is configured.
    print("Khalti key configured:", bool(settings.KHALTI_SECRET_KEY))
    print("Settings module:", settings.SETTINGS_MODULE)

    # Convert rupees into paisa for Khalti.
    amount_in_paisa = int(paid_amount * 100)

    # Payment initiation data.
    payload = {
        "return_url": "http://localhost:8000/payment/verify/",
        "website_url": "http://localhost:8000/",
        "amount": amount_in_paisa,
        "purchase_order_id": str(fee.id),
        "purchase_order_name": f"Fee payment for {fee.course}",
        "customer_info": {
            "name": str(fee.student),
            "email": "test@gmail.com",
            "phone": "9800000005",
        },
    }

    # Khalti authorization headers.
    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            "https://dev.khalti.com/api/v2/epayment/initiate/",
            json=payload,
            headers=headers,
            timeout=20,
        )

        response.raise_for_status()
        data = response.json()

        payment_url = data.get("payment_url")
        pidx = data.get("pidx")

        if not payment_url or not pidx:
            return HttpResponse(
                "Khalti did not return the required payment details.",
                status=502,
            )

        # Save the payment as pending until verification.
        PaymentModel.objects.create(
            student=fee.student,
            fee=fee,
            amount=paid_amount,
            payment_method="Khalti",
            pidx=pidx,
            transaction_id=None,
            status=Status.PENDING,
        )

        # Redirect the user to Khalti's payment page.
        return redirect(payment_url)

    except (requests.RequestException, ValueError):
        return HttpResponse(
            "Failed to initiate Khalti payment. Please try again.",
            status=502,
        )
