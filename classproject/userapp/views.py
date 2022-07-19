from datetime import datetime
import django
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import  staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models.query import InstanceCheckMeta
from django.db import transaction
from django.dispatch.dispatcher import receiver
from django.forms.widgets import DateTimeBaseInput
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views import generic
# from classproject.userapp.forms import 
from classproject.store.forms import Staffform, Userform, Product_form, SignUpForm, customerform
from classproject.store.models import Product_table, Profile
from classproject.store.models import Product_table, staff_table
# Create your views here.

            
@login_required
def customer_update(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = Userform(request.POST, instance=user)
        customer_form =customerform(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid and customer_form.is_valid:
            user_form.save()
            customer_form.save()
            messages.success(request, ('Your Profile Has Been Saved Sucessfully'))
            return HttpResponsePermanentRedirect(reverse('profile', request.user.id))
        else:
            messages.error(request, ('Please Correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('customer_update', request.user.id))
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = Userform(instance=user)
        customer_form =customerform(instance=user.profile)
    return render(request, 'userapp/user_update_form.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

