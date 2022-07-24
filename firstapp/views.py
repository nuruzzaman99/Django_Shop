from time import process_time_ns
from traceback import print_tb
from cv2 import add
from django.shortcuts import redirect, render
from django.views import View
from numpy import product
from firstapp.models import customer, items
from firstapp.models import category, order
from django.contrib.auth.models import User

# Create your views here.
class index(View):
    def post(self, request):
        items = request.POST.get('items')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(items)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(items)
                    else:
                        cart[items] = quantity - 1
                else:
                    cart[items] = quantity + 1
            else:
                cart[items] = 1
        else:
            cart = {}
            cart[items] = 1
        
        request.session['cart'] = cart

        return redirect('shop')

    def get(self_, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        item = items.objects.all()
        categories = category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
            item = items.objects.filter(cat = category_id)
            return render(request, 'shop.html', {'name' : 'Our Shop', 'item' : item, 'categories' : categories})

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

def cart(request):
    ids = list(request.session.get('cart').keys())
    item = items.objects.filter(id__in = ids)

    return render(request, 'cart.html', {'name' : 'Shoping Cart', 'item' : item})


def checkout(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')

        request.session['email'] = email

        cart = request.session.get('cart')
        product = items.objects.filter(id__in = list(cart.keys()))

        if User.objects.filter(email = email).exists():
            if customer.objects.filter(email = email).exists():
                Customer = customer.objects.filter(email = email).first()                
                for item in product:
                    Order = order(items = item,  customer = Customer, price = item.price, quantity = cart.get(str(item.id)))
                    Order.save();
                
                request.session['cart'] = {}
                return redirect('orderlist')
            else:
                Customer = customer(name = name, email = email, address = address, phone = phone)
                Customer.save();
                for item in product:
                    Order = order(items = item,  customer = Customer, price = item.price, quantity = cart.get(str(item.id)))
                    Order.save();
                request.session['cart'] = {}
                return redirect('orderlist')
        else:
            Customer = customer(name = name, email = email, address = address, phone = phone)
            Customer.save();
            for item in product:
                Order = order(items = item,  customer = Customer, price = item.price, quantity = cart.get(str(item.id)))
                Order.save()
            request.session['cart'] = {}
            return redirect('orderlist')

    else:
        ids = list(request.session.get('cart').keys())
        item = items.objects.filter(id__in = ids)

        return render(request, 'checkout.html', {'name' : 'Checkout', 'item' : item})


def orderlist(request):
    Customer = customer.objects.filter(email = request.session.get('email')).first()
    orders = order.objects.filter(customer = Customer).order_by('-date')

    return render(request, 'orderlist.html', {'name' : 'Orders', 'orders' : orders})
