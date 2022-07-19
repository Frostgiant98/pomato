from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from classproject.store import views as store_views

# Create your views here.
urlpatterns = [
    url(r'^product_form/', store_views.product_submit, name="Upload_product"),
    url(r'^product_description/(?P<prod_id>\d+)/', store_views.product_description, name="product_desc" ),
    url(r'^manage_product/', store_views.manageproduct, name="manageprod" ),
    url(r'^delete_product/(?P<prod_id>\d+)/', store_views.deleteproduct, name="deleteprod" ),
    url(r'^approve_product/(?P<prod_id>\d+)/', store_views.approveproduct, name="approveprod" ),
    url(r'^edit_product/(?P<prod_id>\d+)/', store_views.edit_product, name="editprod" ),
    url(r'^user_profile/(?P<user_id>\d+)/', store_views.user_profile, name="userprofile" ),
    url(r'^staff_display/$', store_views.staff_display, name="staff_display" ),
    url(r'^staff_update/(?P<user_id>\d+)/', store_views.staff_update, name="staff_update" ),



]
