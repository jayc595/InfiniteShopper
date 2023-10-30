from django.shortcuts import render, redirect
from .form import RegisterForm
from .models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]  # for now a customer username we will split their email and use before the @

            user = User.objects.create_user(firstname=firstname, lastname=lastname, email=email, username=username, password=password)
            user.phone = phone
            user.save()
            messages.success(request, "Account successfully created")
            return redirect('register')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return
