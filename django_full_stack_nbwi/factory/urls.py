from django.urls import path
from factory.views import FactoryView, OwnerDetail, OwnerView, FactoryAdd, FactoryDetail, OwnerAdd


urlpatterns = [
    path('factory/', FactoryView.as_view(), name="factory"),
    path('factory/add/', FactoryAdd.as_view(), name="addFactory"),
    path('factory/edit/<str:ref_id>/', FactoryDetail.as_view(), name="editFactory"),
    path('owner/', OwnerView.as_view(), name='owner'),
    path('owner/add/', OwnerAdd.as_view(), name="addOwner"),
    path('owner/edit/<int:pk>/', OwnerDetail.as_view(), name="editOwner")
]
