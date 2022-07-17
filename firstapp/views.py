from django.shortcuts import render
from django.http import HttpResponse

from firstapp.models import items
from firstapp.models import category



# Create your views here.
def index(request):

    item = items.objects.all()
    categories = category.objects.all()

    return render(request, 'index.html', {'item' : item, 'categories' : categories})

def shop(request):
    
    return render(request, 'shop.html')