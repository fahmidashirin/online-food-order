from django.contrib import admin
from .models import Category,Products,Profile,Cart,CartItem

# Register your models here.
admin.site.register(Category),
admin.site.register(Products),
admin.site.register(Profile),
admin.site.register(Cart),
admin.site.register(CartItem),