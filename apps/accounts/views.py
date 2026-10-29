from django.contrib.auth.decorators import login_required
from apps.students.models import Student
from apps.attendance.models import AttendanceModel, Status
from apps.fees.models import FeesModel
from apps.payments.models import PaymentModel
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_portal")

            try:
                role = user.userprofile.role
            except Exception:
                messages.error(request, "Your account profile is missing.")
                return redirect("login")

            if role == "ADMIN":
                return redirect("admin_portal")
            elif role == "TEACHER":
                return redirect("staff_portal")
            elif role == "STUDENT":
                return redirect("student_portal")

            messages.error(request, "Invalid account role.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")







@login_required(login_url="/accounts/login/")
def profile_view(request):
    student = get_object_or_404(Student, user=request.user)

    attendance = AttendanceModel.objects.filter(student=student).order_by("-date")
    fees = FeesModel.objects.filter(student=student).select_related("course")
    payments = PaymentModel.objects.filter(student=student).select_related("fee", "fee__course").order_by("-payment_date")

    context = {
        "student": student,
        "attendance": attendance,
        "total_days": attendance.count(),
        "present_days": attendance.filter(status=Status.PRESENT).count(),
        "fees": fees,
        "fees_total_due": fees.aggregate(total=Sum("remaining_amount"))["total"] or 0,
        "first_unpaid_fee": fees.filter(remaining_amount__gt=0).order_by("due_date").first(),
        "payments": payments,
    }

    return render(request, "accounts/profile.html", context)
