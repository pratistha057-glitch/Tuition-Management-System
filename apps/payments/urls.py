from django.urls import path
from apps.payments.services import process_khalti_payment
from apps.payments.views import khalti_verify_view, pay_fee_view, test_payment_page

urlpatterns = [
    path('fees/<int:fee_id>/pay/',pay_fee_view,name='pay-fee'),
    path('fees/<int:fee_id>/process_payment/',process_khalti_payment,name='process-khalti-payment'),
    path('verify/',khalti_verify_view,name='khalti-verify'),
    path("test/",test_payment_page,name="test-payment"),
]
