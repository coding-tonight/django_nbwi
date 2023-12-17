from django.urls import path
from billing.views import BillingView, PrintInvoice


urlpatterns = [
    path('invoice/', BillingView.as_view(), name="invoice"),
    path('print/invoice/', PrintInvoice.as_view(), name="printInvoice")
]
