
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('about', views.about, name='about')

]
