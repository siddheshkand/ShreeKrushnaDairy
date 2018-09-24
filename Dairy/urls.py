from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dairy_home),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout')
]
