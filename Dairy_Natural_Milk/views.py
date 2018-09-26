from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Dairy_Natural_Milk/home.html")
