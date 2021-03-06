from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm


# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('profile')


class PasswordsResetView(PasswordResetView):
    from_class = PasswordResetForm
    success_url = reverse_lazy('profile')
