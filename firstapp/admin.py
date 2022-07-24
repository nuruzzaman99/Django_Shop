from django.contrib import admin
from .models import category, items, customer, order

class AdminItems(admin.ModelAdmin):
    list_display = ['name', 'price', 'cat']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'totalitem']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'quantity']

# Register your models here.
admin.site.register(items, AdminItems)
admin.site.register(category, AdminCategory)
admin.site.register(customer, AdminCustomer)
admin.site.register(order, AdminOrder)