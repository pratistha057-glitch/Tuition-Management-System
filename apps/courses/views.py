from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.courses.models import Course, Subject
from apps.courses.forms import CourseForm, SubjectForm
from apps.accounts.mixins import AdminRequiredMixin


# Course Views
class CourseListView(AdminRequiredMixin, ListView):
    model = Course
    template_name = "courses/index.html"
    context_object_name = "courses"
    ordering = ["name"]


class CourseCreateView(AdminRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/create.html"
    success_url = reverse_lazy("course-list")


class CourseUpdateView(AdminRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/update.html"
    success_url = reverse_lazy("course-list")


class CourseDeleteView(AdminRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/delete.html"
    success_url = reverse_lazy("course-list")




# Subject Views
class SubjectListView(AdminRequiredMixin, ListView):
    model = Subject
    template_name = "subjects/index.html"
    context_object_name = "subjects"
    ordering = ["name"]


class SubjectCreateView(AdminRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/create.html"
    success_url = reverse_lazy("subject-list")


class SubjectUpdateView(AdminRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/update.html"
    success_url = reverse_lazy("subject-list")


class SubjectDeleteView(AdminRequiredMixin, DeleteView):
    model = Subject
    template_name = "subjects/delete.html"
    success_url = reverse_lazy("subject-list")



