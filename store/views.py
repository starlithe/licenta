from core.forms import SearchFormPost
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .models import Category, Product, Frizer, Pachet, Produs, Cart, Comanda

from .forms import SearchForm
from django.db.models import Q

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    celemaivizitate = Produs.objects.filter(vizitate='Cel mai vizitat')
    frizeri = Frizer.objects.all()
    pachete = Pachet.objects.all()
    return render(request, 'store/home.html', {'vizitate': celemaivizitate, 'frizeri': frizeri, 'pachete': pachete})


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
    produse3 = Produs.objects.filter(categorie='Foarfece')
    produse4 = Produs.objects.filter(categorie='Accesorii')
    return render(request, 'store/produse.html', {'produse': produse, 'produse1': produse1, 'produse2': produse2, 'produse3': produse3, 'produse4': produse4})

def produs_detail(request, slug):
    produs = get_object_or_404(Produs, slug=slug)
    return render(request, 'store/products/detail.html', {'produs': produs})


def frizer_detail(request, slug):
    frizer = get_object_or_404(Frizer, slug=slug)
    return render(request, 'store/frizeri_detail.html',{"frizer":frizer})

def search(request):
    produsecautate = Produs.objects.all()
    return render(request, 'store/search.html',{"produsecautate":produsecautate})

def cart(request):
    produse_cart = Cart.objects.filter()
    total=0
    for produs in produse_cart.all():
        total = total+ produs.cart.price*produs.quantity

    return render(request, 'store/cart.html', {"produse_cart": produse_cart, "total":total})


def add_cart(request):
    if request.method == "POST":
        if request.POST.get('action') == "add":
            id = int(request.POST.get("produsid"))
            cantitate = int(request.POST.get("quantity"))
            produs = get_object_or_404(Produs, id=id)
            

            Cart.objects.create(utilizator=request.user, cart=produs, quantity=cantitate)

        return JsonResponse({"succes": "succes"})

def delete_cart(request):
    if request.method == "POST":
        if request.POST.get('action') == "delete":
            id = int(request.POST.get("produsid"))
            cart = get_object_or_404(Cart, id=id)
            cart.delete()

        return JsonResponse({"delete": "delete"})


def programare(request):


    return render(request, 'store/programare.html',{})

def test(request):

    return render(request, 'store/test.html', {})

def search_global(request):

    form = SearchForm()
    q = ''
    results = []
    query = Q()

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            if q is not None:
                query &= (Q(user__username__icontains=q) | Q(title__icontains=q))

            results = Produs.objects.filter(query)

        return redirect(request, 'store/search.html', {'form': form, 'q': q, 'results': results})


def create_appointment(request):
    error = ''
    form = comandaForm()
    if request.method == 'POST':
        form = ComandaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "comanda nu s-a putut efectua! Reincercati!"

    template_name = 'store/comanda.html'

    return render(request, template_name, {'form': form, 'error': error})
