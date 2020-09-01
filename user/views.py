from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from user.forms import RegistrationForm


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('period_list')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                return redirect('login')
    context = {
        'form': forms
    }
    return render(request, 'user/signup.html', context)


def signout(request):
    logout(request)
    return redirect('login')