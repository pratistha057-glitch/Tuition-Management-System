from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.courses.models import Course, Subject
from apps.courses.forms import CourseForm, SubjectForm


# Course Views
class CourseListView(ListView):
    model = Course
    template_name = "courses/index.html"
    context_object_name = "courses"
    ordering = ["name"]


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/create.html"
    success_url = reverse_lazy("course-list")


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/update.html"
    success_url = reverse_lazy("course-list")


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/delete.html"
    success_url = reverse_lazy("course-list")




# Subject Views
class SubjectListView(ListView):
    model = Subject
    template_name = "courses/subjects/index.html"
    context_object_name = "subjects"
    ordering = ["name"]


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "courses/subjects/create.html"
    success_url = reverse_lazy("subject-list")


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "courses/subjects/update.html"
    success_url = reverse_lazy("subject-list")


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "courses/subjects/delete.html"
    success_url = reverse_lazy("subject-list")



