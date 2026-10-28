from decimal import Decimal
import requests
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from apps.fees.models import FeesModel
from apps.payments.models import PaymentModel, Status


def pay_fee_view(request, fee_id):
    fee = get_object_or_404(FeesModel, pk=fee_id)

    return render(request,'payments/pay_fee.html',{'fee': fee})


def khalti_verify_view(request):
    pidx = request.GET.get('pidx')

    if not pidx:
        return HttpResponse(
            "Invalid request: Missing pidx.",
            status=400
        )

    payment_record = get_object_or_404(PaymentModel,pidx=pidx)

    # Do not apply the same payment twice.
    if payment_record.status == Status.SUCCESS:
        return redirect('fee-list')

    if not settings.KHALTI_SECRET_KEY:
        return HttpResponse(
            "Khalti secret key is not configured.",
            status=500
        )

    lookup_url = "https://dev.khalti.com/api/v2/epayment/lookup/"

    headers = {
        "Authorization": f"Key {settings.KHALTI_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            lookup_url,
            json={"pidx": pidx},
            headers=headers,
            timeout=20,
        )

        response.raise_for_status()
        data = response.json()

    except (requests.RequestException, ValueError):
        return HttpResponse(
            "Could not verify the payment with Khalti. Please try again.",
            status=502
        )

    if data.get("status") != "Completed":
        payment_record.status = Status.FAILED
        payment_record.save(update_fields=["status"])

        return HttpResponse(
            f"Payment was not completed. "
            f"Khalti status: {data.get('status', 'Unknown')}",
            status=400
        )

    # Check that the amount confirmed by Khalti matches our record.
    try:
        confirmed_amount = Decimal(str(data["total_amount"]))
    except (KeyError, ValueError, TypeError):
        return HttpResponse(
            "Khalti returned an invalid payment amount.",
            status=502
        )

    expected_amount = payment_record.amount * 100

    if confirmed_amount != expected_amount:
        return HttpResponse(
            "Payment amount does not match the fee record.",
            status=400
        )

    # Update the payment and fee together.
    with transaction.atomic():
        payment_record = PaymentModel.objects.select_for_update().get(
            pk=payment_record.pk
        )

        # Check again in case another verification completed first.
        if payment_record.status == Status.SUCCESS:
            return redirect('fee-list')

        fee_record = FeesModel.objects.select_for_update().get(
            pk=payment_record.fee_id
        )

        payment_record.status = Status.SUCCESS
        payment_record.transaction_id = data.get("transaction_id")
        payment_record.save(
            update_fields=["status", "transaction_id"]
        )

        fee_record.paid_amount += payment_record.amount

        if fee_record.paid_amount >= fee_record.total_amount:
            fee_record.status = "Paid"
        else:
            fee_record.status = "Partially Paid"

        fee_record.save()

    return redirect('fee-list')




def test_payment_page(request):
    fees = FeesModel.objects.select_related(
        "student",
        "course",
    ).all()

    return render(
        request,
        "payments/test_payment.html",
        {"fees": fees},
    )