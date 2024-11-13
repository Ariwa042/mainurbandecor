# products/admin.py
from django.contrib import admin
from .models import Product, Category
from .forms import ProductForm, CategoryForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'is_available']
#    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
