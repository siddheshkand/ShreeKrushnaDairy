from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/dairy/login')
def dairy_home(request):
    return render(request, "Dairy/dairy_home.html")


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dairy/')
    return render(request, 'Dairy/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/dairy/')