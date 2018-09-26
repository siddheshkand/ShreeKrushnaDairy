from django.shortcuts import render
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Home.models import UserForm


# Create your views here.
@login_required(login_url='/dairy/login')
def dairy_home(request):
    user_forms = UserForm.objects.all()
    item_dict = {}
    for user in user_forms:
        item_list = user.item.split(",")
        for item in item_list:
            if item in item_dict:
                item_dict[item] += 1
            else:
                item_dict[item] = 1

    print(item_dict)
    return render(request, "Dairy/dairy_home.html", {'dict': item_dict})


def login_user(request):
    logout(request)
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
