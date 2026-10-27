from django.urls import path
from apps.students.api.views import StudentView, UpdateStudentView


urlpatterns = [
    path("", StudentView.as_view()),
    path("<int:id>", UpdateStudentView.as_view()),
]