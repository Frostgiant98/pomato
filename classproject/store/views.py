import django
from django.db.models.query import InstanceCheckMeta
from django.dispatch.dispatcher import receiver
from django.forms.widgets import DateTimeBaseInput
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from classproject.store.forms import SignUpForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, request
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import SignUpForm
from .forms import Staffform, Userform, Product_form, SignUpForm, customerform
from .models import Product_table, Profile
from django.urls import reverse_lazy
from django.views import generic
from datetime import datetime
from django.utils import timezone
from classproject.store.models import Product_table, staff_table
from classproject.paymentapp.models import Order_table
from classproject.paymentapp.forms import AddToCart_form
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.contrib.admin.views.decorators import  staff_member_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
status = ""

@login_required
def product_submit(request):
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)

        if form.is_valid():
            product_name = form.cleaned_data['product_name']  
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            picture = form.cleaned_data['profile_picture']
            post = Product_table(product_name=product_name, quantity=quantity, price=price, description=description, profile_picture = picture, status = 'Unapproved')
            post.user_id = request.user.id
            post.datetime = timezone.now()
            post.save()
        return HttpResponsePermanentRedirect(reverse('manageprod'))

    else:
        form = Product_form()
        return render(request=request, template_name='store/product_upload.html', context={'form_label':form})
        
class SignUpView(generic.CreateView):
    
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def product_display(request):
    product_detail = Product_table.objects.only('product_id', 'product_name', 'price', 'description', 'profile_picture').filter(status= 'Approved')
    return render(request, 'index.html', {'product':product_detail})


def product_description(request, prod_id):

    '''
    initial was just for showing the product description and it was ...

    product_detail = Product_table.objects.all().filter(status= 'Approved')
    return render(request, 'product.html', {'product':product_detail})

    '''
    
    if request.method == 'POST':
        form = AddToCart_form(request.POST)
        if form.is_valid():
            product_price = Product_table.objects.only('price').filter(product_id= prod_id)
            quantity = form.cleaned_data["quantity"]
            price = product_price.values()[0]['price']
            total_price = "{:.2f}".format(float(quantity) * float(price))
    
        post = Order_table(price=total_price, quantity=quantity)
        post.user_id = request.user.id
        post.date_upload = timezone.now()
        post.product_id = prod_id
        post.save()
        return HttpResponsePermanentRedirect(reverse('cart_prod'))  
    else:
        form = AddToCart_form()
        product_details = Product_table.objects.get(product_id=prod_id)
        
        content = {'form':form, "product":product_details}
        return render(request=request, template_name='store/product_description.html', context={'content' : content})


@login_required
def manageproduct(request):
    products_info = Product_table.objects.all()
    status = products_info.values("status")
    return render(request, 'store/manage_product.html' , {'product': products_info}) 

@login_required
def deleteproduct(request, prod_id):
    Product_table.objects.filter(product_id=prod_id).delete()
    return manageproduct(request)

@login_required
def approveproduct(request, prod_id):
    product_info = Product_table.objects.get(product_id=prod_id)
    if product_info.status == "Unapproved":
        product_info.status = "Approved"
    else:
        product_info.status = "Unapproved"
    product_info.save()
    return manageproduct(request)

def product_view(request):
    product_detail = Product_table.objects.all().filter(status= 'Approved')
    return render(request, 'product.html', {'product':product_detail})

@login_required
def edit_product(request, prod_id):
    edit = get_object_or_404(Product_table, product_id = prod_id)
    form = Product_form(request.POST or None, request.FILES or None, instance=edit)
    if request.method == 'POST':
        if(form.is_valid):
            form.save()
            return manageproduct(request)
    template_name = "store/product_update.html"
    return render(request, template_name, context = {"productupdateform":form})

@login_required
def staff_display(request):
    product_detail = staff_table.objects.all()
    return render(request, 'product.html', {'product':product_detail})

@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def deleteuser(request, user_id):
    User.objects.filter(id=user_id).delete()
    return staff_display(request)

@login_required
def staff_update(request, user_id):
    edit = get_object_or_404(staff_table, user = user_id)
    form = Product_form(request.POST or None, request.FILES or None, instance=edit)
    if request.method == 'POST':
        if(form.is_valid):
            form.save()
            return manageproduct(request)
    template_name = "store/product_update.html"
    return render(request, template_name, context = {"productupdateform":form})

@login_required
def user_profile(request, user_id):
    user_inform = User.objects.all().filter(id = user_id)
    return render(request, 'userapp/user.html', {'person':user_inform})
    


@login_required
@transaction.atomic

# def staff_update(request, user_id):
#     if request.method == 'POST':
#         user_form = userform(request.POST, instance = user_id)
#         profile_form = staffform(request.POST or None, request.FILES or None)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Your Profile Was Saved Sucessfullly'))
#             return HttpResponsePermanentRedirect(reverse('staff_update'))
#         else:
#             messages.error(request, ('Please Correct and fill the invalid Fields'))
#             return HttpResponsePermanentRedirect(reverse('staff_update'))
#     else:
#         user_form = userform(instance= user_id )
#         profile_form = staffform(instance= user_id.profile)
#     return render(request, 'store/staff_update_form.html',{
#         'user_form':user_form,
#         'profile_form': profile_form
#     })
            
@login_required
def staff_update(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = Userform(request.POST, instance=user)
        Profile_form =Staffform(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid and Profile_form.is_valid:
            user_form.save()
            Profile_form.save()
            messages.success(request, ('Your Profile Has Been Saved Sucessfully'))
            return HttpResponsePermanentRedirect(reverse('staff_update', user_id))
        else:
            messages.error(request, ('Please Correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('staff_update', user_id))
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = Userform(instance=user)
        Profile_form =Staffform(instance=user.profile)
    return render(request, 'store/staff_update_form.html', {
        'user_form': user_form,
        'profile_form':Profile_form
    })



@login_required
def staff_display(request):
    
    user_inform = User.objects.all()
    return render(request, 'userapp/manage_staff.html', {'user':user_inform})

