from django.urls import path
from . import views

urlpatterns = [
    
    path('registration', views.registration, name='registration'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]