# from typing_extensions import Required
# from django.urls.base import reverse

from django.urls.base import reverse
from django.utils import timezone
from django.utils.translation import TranslatorCommentWarning
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
# from .forms import Product_form
from .models import Invoice_table, Product_table
from .forms import AddToCart_form, CardDetails_form, paymentOption_form

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, request
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.db import transaction

from classproject.paymentapp.models import Order_table

# Create your views here.

total_price = 0

@login_required
def cart_(request,):
    cart_info = Order_table.objects.filter(user_id=request.user.id)
    # status = cart_info.values("status")
    return render(request, 'payment/user_cart.html' , {'cart': cart_info}) 

@login_required
def deleteorder(request, ord_id):
    Order_table.objects.filter(order_id=ord_id ).delete()
    return cart_(request)

@login_required
def editorder(request, ord_id):
    global total_price
    edit = get_object_or_404(Order_table, order_id = ord_id)
    form = AddToCart_form(request.POST or None, request.FILES or None, instance=edit)
    if request.method == 'POST':
        if(form.is_valid):
            form.save()
            details = Order_table.objects.get(order_id=ord_id)
            price = "{:.2f}".format(float(details.quantity) * float(total_price))
            Order_table.objects.filter(order_id=ord_id).update(price=price)
            return cart_(request)
    product_details = Product_table.objects.get(product_id=edit.product_id)
    total_price = product_details.price
    content = {'form':form, "product":product_details}
    template_name = "store/product_description.html"
    return render(request, template_name, context = {"content":content})

@login_required
def order_Recipt(request, user_id):
    price = 0
    order = Order_table.objects.filter(user_id = user_id)
    for value in order.values():
        price += float(value['price'])
    receipt = Invoice_table(date_cashout = timezone.now(), user_id= user_id, total_price = price) 
    receipt.save()
    receipt_details = Invoice_table.objects.filter(user_id=user_id,cashout=False)
    return render(request, template_name='paymentapp/recipt.html', context={"recipt":receipt_details.values()[0], 'order':order})

@login_required
def payment_services(request, user_id):
    form = paymentOption_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            option = form.cleaned_data['option']
            if option == 'payOnDelivery':
                receipt_details = Invoice_table.object.filter(user_id = user_id, cashout=False)
                return render(request, template_name="paymentapp/success_pay.html", context={"reciept": receipt_details.values()[0]})
            else:
                return HttpResponsePermanentRedirect(reverse('card_detail', args=(user_id)))
        else:
            form = paymentOption_form()
            receipt_details = Invoice_table.object.filter(user_id=user_id, cashout=False)
            return render(request, template_name="paymentapp/payment_service.html", context={"form":form, "receipt":receipt_details.values()[0]})

@transaction.atomic
@login_required
def card_details(request, user_id):
    form =CardDetails_form(request.POST)
    if request.method == "POST":
        if form.is_valid:
            cardName = form.cleaned_data['card_name']
            cardNumber = form.cleaned_data['card_number']
            cardCvv = form.cleaned_data['card_cvv']
            cardExpiryDate = form.cleaned_data['card_expiry_date']
        order = Order_table.objects.filter(user_id=user_id, purchased=False).update(cahout=True)
        return render(request, template_name="paymentapp/success_pay")
    else:
        form = CardDetails_form()
        return render(request, template_name="payment/card_detail.html", context={"form":form})

@login_required
def delete_invoice(request, user_id):
    Invoice_table.objects.filter(user_id=user_id, cashout=False).delete()
    return cart_(request)

