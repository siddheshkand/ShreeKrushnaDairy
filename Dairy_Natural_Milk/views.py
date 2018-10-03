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
    return render(request, "Dairy_Natural_Milk/Fill_Information/fill_information_home.html")


# Bank Views
@login_required(login_url='/dairy/login')
def bank_home(request):
    transaction_info = models.Transaction.objects.all()
    return render(request, "Dairy_Natural_Milk/Fill_Information/Bank/bank_home.html",
                  {'transaction_info': transaction_info})


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
    return render(request, "Dairy_Natural_Milk/Fill_Information/Bank/create_transaction.html",
                  {'form': form, 'message': message})


# Printing View
@login_required(login_url='/dairy/login')
def printing_home(request):
    return render(request, 'Dairy_Natural_Milk/Printing/printing_home.html')


@login_required(login_url='/dairy/login')
def new_account(request):
    message = ""
    account_info = models.Account.objects.all()
    if request.method == "POST":
        form = forms.CreateNewAccount(request.POST)
        if form.is_valid():
            form.save()
            message = "Customer Saved"
    else:
        form = forms.CreateNewAccount()
    return render(request, "Dairy_Natural_Milk/Fill_Information/New_Account/new_account_home.html", {
        'form': form,
        'message': message,
        'new_account': account_info,
    })


@login_required(login_url='/dairy/login')
def view_customer(request):
    customer_model = models.Account.objects.filter(relation='customer')
    return render(request, "Dairy_Natural_Milk/Printing/customer.html", {'customer_model': customer_model})

