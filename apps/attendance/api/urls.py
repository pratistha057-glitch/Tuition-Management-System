from django.urls import path
from apps.attendance.api.views import AttendanceView, UpdateAttendanceView


urlpatterns = [
    path("", AttendanceView.as_view()),
    path("<int:id>", UpdateAttendanceView.as_view()),
]