from django.urls import path
from apps.fees.api.views import FeeView, UpdateFeeView


urlpatterns = [
    path("", FeeView.as_view()),
    path("<int:id>", UpdateFeeView.as_view()),
]
