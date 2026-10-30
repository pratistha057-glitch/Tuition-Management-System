from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.accounts.mixins import AdminOrTeacherRequiredMixin
from apps.fees.models import FeesModel
from apps.fees.forms import FeeForm


# Fees Views
class FeeListView(AdminOrTeacherRequiredMixin, ListView):
    model = FeesModel
    template_name = "fees/index.html"
    context_object_name = "fees"


class FeeCreateView(AdminOrTeacherRequiredMixin, CreateView):
    model = FeesModel
    form_class = FeeForm
    template_name = "fees/create.html"
    success_url = reverse_lazy("fee-list")


class FeeUpdateView(AdminOrTeacherRequiredMixin, UpdateView):
    model = FeesModel
    form_class = FeeForm
    template_name = "fees/update.html"
    success_url = reverse_lazy("fee-list")


class FeeDeleteView(AdminOrTeacherRequiredMixin, DeleteView):
    model = FeesModel
    template_name = "fees/delete.html"
    success_url = reverse_lazy("fee-list")