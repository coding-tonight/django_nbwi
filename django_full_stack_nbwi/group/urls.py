from django.urls import path
from group.views import GroupDelete, GroupDetail, GroupView, GroupAdd


urlpatterns = [
    path('group/', GroupView.as_view(), name="group"),
    path('group/add/', GroupAdd.as_view(), name="addGroup"),
    path('group/edit/<str:ref_id>/', GroupDetail.as_view(), name="editGroup"),
    path('group/delete/<str:ref_id>/', GroupDelete.as_view(), name="deleteGroup")
]
