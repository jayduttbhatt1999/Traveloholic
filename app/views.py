from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            messages.warning(request, 'Register here')
            return redirect('app:register_page')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('app:index')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'app/login.html')


def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            message.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'app/register.html')


def about(request):
    return render(request, "app/about.html")


def hotels(request):
    return render(request, "app/hotels.html")


def insurance(request):
    return render(request, "app/insurance.html")


def package(request):
    return render(request, "app/packages.html")


def message(request):
    return render(request, "app/messages.html")


def contact(request):
    return render(request, "app/contact.html")
