from django.contrib import admin
from .models import category, items

# Register your models here.
admin.site.register(items)
admin.site.register(category)