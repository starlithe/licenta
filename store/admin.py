from django.contrib import admin

from .models import Category, Product, Frizer, Pachet, Produs, Cart, Comanda


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Produs)
class ProdusAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Frizer)
class FrizerAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Pachet)
class PachetAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Cart)
admin.site.register(Comanda)
