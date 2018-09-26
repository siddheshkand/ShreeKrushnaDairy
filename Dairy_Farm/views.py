from django.shortcuts import render
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Home.models import UserForm


@login_required(login_url='/dairy/login')
def home(request):
    return render(request, "Dairy_Farm/home.html")
