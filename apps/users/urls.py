from django.urls import path
from .views import register, staff
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('staff/',staff, name='staff')
]
