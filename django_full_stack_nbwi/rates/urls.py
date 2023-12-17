from django.urls import path
from rates.views import RateAdd, RateDetail, RateView , RateDelete

urlpatterns = [
    path('rates/', RateView.as_view(), name='rates'),
    path('rates/add/', RateAdd.as_view(), name="addRate"),
    path('rate/edit/<str:ref_id>/', RateDetail.as_view(), name="editRate"),
    path('rate/delete/<str:ref_id>/', RateDelete.as_view() , name="deleteRate")
]
