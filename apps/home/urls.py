from django.urls import path
from apps.home.views import home_view, admin_portal, staff_portal, student_portal

urlpatterns = [
    path("", home_view, name="home"),
    path("admin-portal/", admin_portal, name="admin_portal"),
    path("staff-portal/", staff_portal, name="staff_portal"),
    path("student/portal/", student_portal, name="student_portal"),
]