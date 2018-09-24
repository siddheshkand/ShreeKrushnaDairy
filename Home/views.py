from django.contrib import messages
from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    if request.method == 'POST':
        print("Form submitted")

        instance = models.UserForm()
        instance.name = request.POST.get("name")
        instance.phone = request.POST.get("phone")
        instance.item = ','.join(request.POST.getlist("item"))
        instance.desc = request.POST.get("description")
        instance.save()
        messages.add_message(request, messages.SUCCESS, "आम्ही लवकरच अप्प्ल्याशी संपर्क साधू")

    return render(request, 'Home/index.html')
