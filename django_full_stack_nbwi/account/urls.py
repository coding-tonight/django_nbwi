from django.urls import path
from account.views import AccountDetail, AccountView, AccountAdd , AccountDelete
# from account.views import


urlpatterns = [
    path('account/', AccountView.as_view(), name="account"),
    path('account/add/', AccountAdd.as_view(), name="addAccount"),
    path('account/edit/<str:ref_id>/', AccountDetail.as_view(), name="editAccount"),
    path('account/delete/<str:ref_id>/', AccountDelete.as_view(), name="deleteAccount")
]
