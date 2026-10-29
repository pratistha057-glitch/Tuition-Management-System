from django.urls import path
from apps.attendance.views import mark_attendance

urlpatterns = [
    path("", mark_attendance, name="attendance"),
]
