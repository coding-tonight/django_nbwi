from django.urls import path
from app.views import LoginView , Logout


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/' ,Logout.as_view(),name="logout")
]
