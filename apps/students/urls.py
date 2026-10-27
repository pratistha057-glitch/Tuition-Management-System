from django.urls import path
from apps.students.views import StudentListView,StudentCreateView,StudentUpdateView,StudentDeleteView

urlpatterns = [
    path("", StudentListView.as_view(), name="student-list"),
    path("create/", StudentCreateView.as_view(), name="student-create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),
]
