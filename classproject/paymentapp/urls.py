from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from classproject.store import views as store_views
from classproject.paymentapp import views as payment_views

urlpatterns = [
    url(r'^cart_item/', payment_views.cart_, name="cart_prod" ),
    url(r'^delete_order/(?P<ord_id>\d+)/', payment_views.deleteorder, name="deleteord" ),
    url(r'^edit_order/(?P<ord_id>\d+)/', payment_views.editorder, name="editord" ),
    url(r'^pay_form/(?P<ord_id>\d+)/', payment_views.card_details, name="carddets" ),

]