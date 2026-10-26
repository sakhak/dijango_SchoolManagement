from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.teacher_list, name='list'),

    path('/add/', views.teacher_create, name='create'),

    path(
        '/<int:pk>/',
        views.teacher_detail,
        name='detail'
    ),

    path('/<int:pk>/edit/', views.teacher_update, name='update'),
    path('/<int:pk>/delete/', views.teacher_delete, name='delete'),
]
