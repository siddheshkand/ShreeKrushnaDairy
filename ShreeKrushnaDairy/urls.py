"""ShreeKrushnaDairy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from Home import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.home),
                  url(r'^dairy/', include(('Dairy.urls', 'Dairy'), namespace='dairy')),
                  url(r'^dairy_bachat/', include(('Dairy_Bachat.urls', 'Dairy_Bachat'), namespace='dairy_bachat')),
                  url(r'^dairy_farm/', include(('Dairy_Farm.urls', 'Dairy_Farm'), namespace='dairy_farm')),
                  url(r'^dairy_natural_milk/',
                      include(('Dairy_Natural_Milk.urls', 'Dairy_Natural_Milk'), namespace='dairy_natural_milk')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
