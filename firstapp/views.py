from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from firstapp.models import items
from firstapp.models import category
from django.views.generic import ListView, DetailView



# Create your views here.
class index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = 1 + quantity
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart

        return render(request, 'shopDetails.html', {'name' : 'Shop Details'})

    def get(self, request):
        item = items.objects.all()
        categories = category.objects.all()

        return render(request, 'index.html', {'item' : item, 'categories' : categories})


def shop(request):
    item = items.objects.all()
    categories = category.objects.all()

    return render(request, 'shop.html', {'name' : 'Our Shop', 'item' : item, 'categories' : categories})

def shopDetails(request):
    item = items.objects.all()
    categories = category.objects.all()

    return render(request, 'shopDetails.html', {'name' : 'Shop Details', 'item' : item, 'categories' : categories})

def contact(request):

    return render(request, 'contact.html', {'name' : 'Contacts'})

def checkout(request):

    return render(request, 'checkout.html', {'name' : 'Checkout'})

def cart(request):

    return render(request, 'cart.html', {'name' : 'Shoping Cart'})


class detail(ListView):
    model = items
    template_name = 'index.html'
