"""classproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls import url, include
from .store.views import SignUpView,product_display, product_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_display, name="homepage"),
    path('product', product_view, name="Product"),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('special', TemplateView.as_view(template_name='special.html'), name='special'),
    path('brand', TemplateView.as_view(template_name='brand.html'), name='brand'),
    path('store/landing', TemplateView.as_view(template_name='store/landing.html'), name='landing'),
    path('profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    url(r'^store/', include('classproject.store.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^customer/', include('classproject.userapp.urls')),
    url(r'^pay/', include('classproject.paymentapp.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)