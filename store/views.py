from django.shortcuts import get_object_or_404, render

from .models import Category, Product, Frizer, Pachet, Produs


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    celemaivizitate = Produs.objects.filter(vizitate='Cel mai vizitat')
    frizeri = Frizer.objects.all()
    pachete = Pachet.objects.all()
    return render(request, 'store/home.html', {'vizitate': celemaivizitate, 'frizeri': frizeri, 'pachete': pachete,})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})



def produse(request):
    produse = Produs.objects.filter(categorie='Masini tuns')
    produse1 = Produs.objects.filter(categorie='Masini contur')
    produse2 = Produs.objects.filter(categorie='Shavere')
    return render(request, 'store/produse.html', {'produse':produse, 'produse1':produse1, 'produse2':produse2})

def produs_detail(request, slug):
    produs = get_object_or_404(Produs, slug=slug)
    return render(request, 'store/products/detail.html', {'produs': produs})

def search(request):
    produsecautate = Produs.objects.all()
    return render(request, 'store/search.html',{"produsecautate":produsecautate})