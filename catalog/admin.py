from django.contrib import admin
from catalog.models import Product, Category, Version

admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price'),
    list_filter = ('category',),
    search_fields = ('name', 'description',)


admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Version)


class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
