from django.shortcuts import render, redirect
from .models import Product, Cart, CartItems
from django.http import JsonResponse, HttpResponse
import json
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout


def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      redirect('index')
    else:
      return JsonResponse('Form Is Invalid', safe=False)
  
  form = SignUpForm()
    
  return render(request, 'signup.html', {'form':form})

def logout_view(request):
  logout(request)
  return redirect('login')

def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request,username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('index')
    
  form = LoginForm()
  return render(request, 'login.html', {'form':form})

def index(request):
  
  cart = None
  if request.user.is_authenticated:
    cart, created = Cart.objects.get_or_create(user=request.user, completed= False)
  
  products = Product.objects.all()
  context={'products': products, 'cart': cart}
  return render(request, 'index.html', context)
  
def cart(request):
  cartitems=[]
  cart=None
  if request.user.is_authenticated:
    cart, created = Cart.objects.get_or_create(user=request.user, completed= False)
    cartitems = cart.cartitems.all()
  else:
    print('User is not authenticated')
  context={'cartitems':cartitems, 'cart':cart}
  return render(request, 'cart.html', context)
  
def add_cart(request):
  data = json.loads(request.body)
  id = data["id"]
  product = Product.objects.get(id=id)
  if request.user.is_authenticated:
    cart, created = Cart.objects.get_or_create(user=request.user, completed= False)
    cartitem, created = CartItems.objects.get_or_create(product=product, cart=cart)
    cartitem.quantity += 1
    cartitem.save()
    
    item_number = cart.item_number
    
    
  else:
    print('User is not authenticated')
    
  return JsonResponse(item_number, safe=False)