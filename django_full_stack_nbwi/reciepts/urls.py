from django.urls import path 
from reciepts.views import ReceiptsView, ReceiptsAdd , ReceiptsDetail, ReceiptDelete

urlpatterns = [
    path('receipts/', ReceiptsView.as_view(), name="receipts"),
    path('receipts/add/', ReceiptsAdd.as_view(), name='addReceipt'),
    path('receipts/edit/<str:ref_id>/',ReceiptsDetail.as_view(), name='editReceipt'),
    path('receipts/delete/<str:ref_id>/', ReceiptDelete.as_view(), name='deleteReceipt')
]