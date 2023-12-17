from django.urls import path
from payment.views import PaymentView , PaymentAdd , PaymentDetail

urlpatterns = [
     path('payment/' ,PaymentView.as_view(), name="payment"),
     path('payment/add/' ,PaymentAdd.as_view(), name="addPayment"),
     path('payment/edit/<str:ref_id>/' ,PaymentDetail.as_view(), name="editPayment"),
]