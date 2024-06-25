from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Version)
class Product(admin.ModelAdmin):
    list_display = ("num_of_version", "version_name", "is_active_version")
    list_filter = ("num_of_version",)
    search_fields = ("num_of_version", "version_name","is_active_version",)
