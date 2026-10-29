
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


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
