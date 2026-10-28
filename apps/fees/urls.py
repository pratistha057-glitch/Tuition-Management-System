
from django.urls import path
from apps.fees.views import FeeListView,FeeCreateView,FeeUpdateView,FeeDeleteView


urlpatterns = [
    path("", FeeListView.as_view(), name="fee-list"),
    path("create/", FeeCreateView.as_view(), name="fee-create"),
    path("<int:pk>/update/", FeeUpdateView.as_view(), name="fee-update"),
    path("<int:pk>/delete/", FeeDeleteView.as_view(), name="fee-delete"),
]
