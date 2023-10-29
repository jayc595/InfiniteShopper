from django.shortcuts import render
from .form import RegisterForm


# Create your views here.
def register(request):
    form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return
