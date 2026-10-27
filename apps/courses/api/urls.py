from django.urls import path
from apps.courses.api.views import CourseView, SubjectView, UpdateCourseView, UpdateSubjectView


urlpatterns = [
    path("", CourseView.as_view()),
    path("<int:id>", UpdateCourseView.as_view()),
    path("subjects/", SubjectView.as_view()),
    path("subjects/<int:id>", UpdateSubjectView.as_view()),
]