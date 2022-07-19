from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from classproject.store import views as store_views
from classproject.paymentapp import views as payment_views
from classproject.userapp import views as user_views

urlpatterns = [
    url(r'^customer_update/(?P<user_id>\d+)/', user_views.customer_update, name="customer_update" ),

]