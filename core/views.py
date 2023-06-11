from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import SignupForm
from django.http import JsonResponse
import json, datetime
from .models import *


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        ordname = order.id
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']
        ordname = {'ordname': ''}

    products = Product.objects.all()
    context = {'products': products, 'cartitems': cartitems, 'ordname': ordname}

    return render(request, 'core/index.html', context)