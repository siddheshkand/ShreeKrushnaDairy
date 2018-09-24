from django.shortcuts import render


# Create your views here.
def dairy_home(request):
    return render(request, "Dairy/dairy_home.html")


def login(request):
    return render(request, "Dairy/login.html")