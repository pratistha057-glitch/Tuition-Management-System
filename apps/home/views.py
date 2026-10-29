from django.shortcuts import render

from apps.students.models import Student
from apps.courses.models import Course
from apps.attendance.models import AttendanceModel, Status


# Home page
def home_view(request):
    return render(request, "home/home.html")


# Admin portal
def admin_portal(request):
    recent_students = Student.objects.select_related(
        "user"
    ).order_by("-id")[:5]

    recent_attendance = AttendanceModel.objects.select_related(
        "student",
        "student__user",
    ).order_by("-date", "-id")[:5]

    context = {
        "total_students": Student.objects.count(),
        "total_attendance_records": AttendanceModel.objects.count(),
        "recent_students": recent_students,
        "recent_attendance": recent_attendance,

        # Placeholder until we connect the Fees app
        "pending_fees_list": [],
    }

    return render(request, "home/admin_portal.html", context)


# Staff portal
def staff_portal(request):
    students = Student.objects.select_related(
        "user"
    ).order_by("user__username")

    attendance_records = AttendanceModel.objects.select_related(
        "student",
        "student__user",
    ).order_by("-date", "-id")

    selected_student_id = request.GET.get("student_id", "").strip()

    if selected_student_id:
        if selected_student_id.isdigit():
            attendance_records = attendance_records.filter(
                student_id=int(selected_student_id)
            )
        else:
            attendance_records = attendance_records.none()

    context = {
        "staff_member": request.user,
        "students": students,
        "attendance_records": attendance_records,
        "selected_student_id": selected_student_id,
    }

    return render(request, "home/staff_portal.html", context)


# Student portal
def student_portal(request):
    student = None

    if request.user.is_authenticated:
        student = Student.objects.filter(
            user=request.user
        ).first()

    if student is None:
        context = {
            "student": None,
            "total_days": 0,
            "present_days": 0,
            "attendance_rate": 0,
            "attendance_records": [],
            "pending_fees": [],
        }

        return render(request, "home/student_portal.html", context)

    attendance_records = AttendanceModel.objects.filter(
        student=student
    ).order_by("-date")

    total_days = attendance_records.count()

    present_days = attendance_records.filter(
        status=Status.PRESENT
    ).count()

    attendance_rate = (
        round((present_days / total_days) * 100)
        if total_days > 0
        else 0
    )

    context = {
        "student": student,
        "total_days": total_days,
        "present_days": present_days,
        "attendance_rate": attendance_rate,
        "attendance_records": attendance_records,

        # Placeholder until we connect the Fees app
        "pending_fees": [],
    }

    return render(request, "home/student_portal.html", context)