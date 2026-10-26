from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'core'



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),

]
