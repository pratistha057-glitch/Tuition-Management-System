from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.students.models import Student
from apps.students.forms import StudentForm
from apps.accounts.mixins import AdminRequiredMixin


class StudentListView(AdminRequiredMixin, ListView):
    model = Student
    template_name = "students/index.html"
    context_object_name = "students"
    ordering = ["student_id"]


class StudentCreateView(AdminRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/create.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(AdminRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/update.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(AdminRequiredMixin, DeleteView):
    model = Student
    template_name = "students/delete.html"
    success_url = reverse_lazy("student-list")
