from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Category, Product, Frizer, Pachet, Produs, Cart


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

def cart(request):
    produse_cart = Cart.objects.filter(utilizator=request.user)
    total=0
    for produs in produse_cart.all():
        total = total+ produs.cart.price*produs.quantity

    return render(request, 'store/cart.html', {"produse_cart": produse_cart, "total":total})


def add_cart(request):
    if request.method == "POST":
        if request.POST.get('action') == "add":
            id = int(request.POST.get("produsid"))
            cantitate = int(request.POST.get("quantity"))
            produs = get_object_or_404(Cart, id=id)
            print("daasdas")

            Cart.objects.create(utilizator=request.user, cart=produs, quantity=cantitate)

        return JsonResponse({"succes": "succes"})



