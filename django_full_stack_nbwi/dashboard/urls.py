from django.urls import path
from dashboard.views import DashboardView , ChartData

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('chartdata/',ChartData.as_view(), name="chartData")
]
