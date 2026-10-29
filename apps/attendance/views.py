from django.contrib.auth.decorators import login_required, user_passes_test
from apps.accounts.decorators import is_admin_or_teacher
from django.shortcuts import render, redirect
from django.utils import timezone

from apps.students.models import Student
from .models import AttendanceModel, Status

@login_required
@user_passes_test(is_admin_or_teacher)
def mark_attendance(request):
    selected_date = request.GET.get('date', str(timezone.localdate()))
    students = Student.objects.all()

    if request.method == 'POST':
        selected_date = request.POST.get('date', selected_date)

        for student in students:
            status = request.POST.get(
                f'status_{student.id}',
                Status.ABSENT
            )

            AttendanceModel.objects.update_or_create(
                student=student,
                date=selected_date,
                defaults={'status': status}
            )

        return redirect(f'{request.path}?date={selected_date}')

    attendance = {
        item.student_id: item.status
        for item in AttendanceModel.objects.filter(date=selected_date)
    }

    students_data = [
        {
            'student': student,
            'status': attendance.get(student.id, Status.ABSENT),
        }
        for student in students
    ]

    return render(request, 'attendance/index.html', {
        'students_data': students_data,
        'selected_date': selected_date,
    })
