from django.urls import path
from reports.views import SaleReportView , InventoryWiseView , LedgerReportView , LedgerDetail , SaleOptionView , InventoryWiseView

urlpatterns = [
    path('sale/reports/', SaleOptionView.as_view(), name="salesReport"),
    path('sale/report/bill', SaleReportView.as_view(), name="billReport"),
    path('sale/item/wise/report/',InventoryWiseView.as_view(), name="saleItemWise"),
    path('ledger/report/', LedgerReportView.as_view(), name="ledgerReport"),
    path('ledger/report/<str:ref_id>/', LedgerDetail.as_view(), name="ledgerDetail"),
     #  filter pages
    path('sale/report/wise/report/filter', InventoryWiseView.as_view(), name="saleItemWiseFilter")  
]