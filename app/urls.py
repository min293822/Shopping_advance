from django.urls import path
from . import views

urlpatterns=[
  path('', views.user_login, name='login'),
  path('signup/', views.signup, name='signup'),
  path('logout/', views.logout_view, name='logout'),
  path('index/', views.index, name='index'),
  path('cart/', views.cart, name='cart'),
  path('index/add_cart/', views.add_cart, name='add_cart'),
  ]