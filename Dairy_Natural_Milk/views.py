from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.
@login_required(login_url='/dairy/login')
def home(request):
    return render(request, "Dairy_Natural_Milk/home.html")


# माहिती भरणे
@login_required(login_url='/dairy/login')
def fill_information(request):
    return render(request, "Dairy_Natural_Milk/fill_information.html")


# Bank Views
@login_required(login_url='/dairy/login')
def bank_home(request):
    transaction_info = models.Transaction.objects.all()
    return render(request, "Dairy_Natural_Milk/Bank/bank_home.html", {'transaction_info': transaction_info})


@login_required(login_url='/dairy/login')
def create_transaction(request):
    message = ""
    if request.method == "POST":
        form = forms.CreateTransaction(request.POST)
        if form.is_valid():
            form.save()
            message = "Saved Transaction"
    else:
        form = forms.CreateTransaction()
    return render(request, "Dairy_Natural_Milk/Bank/create_transaction.html", {'form': form, 'message': message})
