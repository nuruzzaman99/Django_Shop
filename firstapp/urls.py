from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('orderlist', views.orderlist, name='orderlist'),
    path('checkout', views.checkout, name='checkout'),
    path('shopDetails', views.shopDetails, name='shopDetails'),
]