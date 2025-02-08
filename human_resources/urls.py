from django.urls import path
from . import views

urlpatterns = [
    path('HR/Login', views.loginHumanResource, name='login'),
]
