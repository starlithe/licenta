from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'store'

urlpatterns = [
    path('home/', views.all_products, name='all_products'),
    path('item1/<str:slug>/', views.produs_detail, name='produs_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('produse/', views.produse, name='produse'),
    path('search/', views.search, name='produsecautate'),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('account/', include ('django.contrib.auth.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)