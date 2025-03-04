from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request) -> HttpResponse:
    """
    View that register the new users
    
    Keyword arguments:
        request -- object that contains the needed http attributes
    Return: a HttpResponse object
    """
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your Account has been created ! {username}")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    """
    Shows the user's profile, the user must be logged in to view this page
    
    Keyword arguments:
        request -- object that contains the needed http attributes
    Return: a HttpResponse object
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Account has been updated !")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)