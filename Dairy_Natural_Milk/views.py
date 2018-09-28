from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/dairy/login')
def home(request):
    return render(request, "Dairy_Natural_Milk/home.html")


# माहिती भरणे
@login_required(login_url='/dairy/login')
def fill_information(request):
    return render(request, "Dairy_Natural_Milk/fill_information.html")


@login_required(login_url='/dairy/login')
def bank_home(request):
    return render(request, "Dairy_Natural_Milk/Bank/bank_home.html")
