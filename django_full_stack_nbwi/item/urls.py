from django.urls import path
from item.views import ItemAdd, ItemView, ItemDetail ,ItemDelete

urlpatterns = [
    path('item/', ItemView.as_view(), name='item'),
    path('item/add', ItemAdd.as_view(), name='addItem'),
    path('item/edit/<str:ref_id>/', ItemDetail.as_view(), name="editItem"),
    path('item/delete/<str:ref_id>/', ItemDelete.as_view(), name="deleteItem")
]
