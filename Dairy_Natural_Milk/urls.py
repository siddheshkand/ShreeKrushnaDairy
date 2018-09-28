from django.conf.urls import url
from . import views

urlpatterns = [
    # General Purpose Url
    url(r'^$', views.home, name='home'),
    url(r'^fill_information/', views.fill_information, name='fill_information'),
    # Bank
    url(r'^bank_home/', views.bank_home, name='bank_home'),
]
