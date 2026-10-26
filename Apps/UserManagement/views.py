from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, ProfileUpdateForm


class CustomLoginView(LoginView):
    template_name = 'usermanagement/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {form.get_user().get_full_name() or form.get_user().username}!")
        return super().form_valid(form)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully. Welcome!")
            return redirect('core:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'usermanagement/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('usermanagement:login')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('usermanagement:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'usermanagement/profile.html', {'form': form})


@login_required
def user_list_view(request):
    from .models import User
    if not request.user.is_admin:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('core:dashboard')
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'usermanagement/user_list.html', {'users': users})
