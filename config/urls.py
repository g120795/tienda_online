"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from .views import home, features, about_us, contact, product, order, catalog_link, seller_function, staff_link
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name='home'),
    path('home/features/',features, name='features'),
    path('home/about_us/', about_us, name='about_us'),
    path('home/contact/', contact, name='contact'),
    path('home/features/product', product, name='product'),
    path('home/features/staff_link', staff_link, name='staff_link'),
    path('home/features/order', order, name='order'),
    path('home/features/catalog_link', catalog_link, name='catalog_link'),
    path('app/store/', include('apps.store.urls'),name='store'),
    path('app/users/', include('apps.users.urls'),name='users'),
    path('home/seller_funtion/', seller_function, name='seller_function'),
    path('accounts/', include('django.contrib.auth.urls')),

]
