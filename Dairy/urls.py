from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dairy_home),
    url(r'^login/$', views.login)
]
