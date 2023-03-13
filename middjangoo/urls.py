"""middjangoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from middjangoo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='my-index'),
    path('bookings',views.booking,name='my-bookings'),
    path('gallery',views.gallery,name='my-gallery'),
    path('restaurant',views.restaurant,name='my-restaurant'),
    path('services',views.services,name='my-services'),
    path('login',views.login,name='my-login'),
    path('signup',views.signup,name='my-signup'),
    path('testimonial',views.testimonial,name='my-testimonial'),
    path('edit',views.edit,name='my-edit')
]
