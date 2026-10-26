from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usermanagement'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('users/', views.user_list_view, name='user_list'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='usermanagement/password_change.html',
        success_url='/accounts/profile/'
    ), name='password_change'),
]
