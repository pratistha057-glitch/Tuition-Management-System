from django.urls import path
from apps.courses.views import (
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    SubjectListView,
    SubjectCreateView,
    SubjectUpdateView,
    SubjectDeleteView,
    BatchListView,
    BatchCreateView,
    BatchUpdateView,
    BatchDeleteView,
)

urlpatterns = [
    # Course URL
    path("", CourseListView.as_view(), name="course-list"),
    path("create/", CourseCreateView.as_view(), name="course-create"),
    path("<int:pk>/update/", CourseUpdateView.as_view(), name="course-update"),
    path("<int:pk>/delete/", CourseDeleteView.as_view(), name="course-delete"),

    # Subject URL
    path("subjects/", SubjectListView.as_view(), name="subject-list"),
    path("subjects/create/", SubjectCreateView.as_view(), name="subject-create"),
    path("subjects/<int:pk>/update/", SubjectUpdateView.as_view(), name="subject-update"),
    path("subjects/<int:pk>/delete/", SubjectDeleteView.as_view(), name="subject-delete"),

    # Batch URL
    path("batches/", BatchListView.as_view(), name="batch-list"),
    path("batches/create/", BatchCreateView.as_view(), name="batch-create"),
    path("batches/<int:pk>/update/", BatchUpdateView.as_view(), name="batch-update"),
    path("batches/<int:pk>/delete/", BatchDeleteView.as_view(), name="batch-delete"),
]
