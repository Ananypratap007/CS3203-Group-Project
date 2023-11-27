from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.core import serializers
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode
from .forms import SignupForm
from .models import Product, Cart, CartItem
from django.http import JsonResponse
import json
from django.contrib import messages


def home(request):
    return render(request, "menu.html")

def menu(request):
    products = Product.objects.all()
    
    cart = None

    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user, completed=False)
        
    context = {"products" : products, "cart" : cart}
    return render(request, "menu.html", context)

def profile(request):
    return render(request, "profile.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def cart(request):
    cart = None
    cartitems = []
    
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    
    context = {"cart":cart, "items":cartitems}
    return render(request, "cart.html", context)

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem =CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        
        
        num_of_item = cart.num_of_items
        
        print(cartitem)
    return JsonResponse(num_of_item, safe=False)


def confirm_payment(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.completed = True
    cart.save()
    messages.success(request, "Payment made successfully")
    return redirect("menu")

