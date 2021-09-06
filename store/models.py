import uuid
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Frizer(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Frizeri'

    def get_absolute_url(self):
        return reverse('store:frizeri_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Pachet(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Pachete'

    def __str__(self):
        return self.title



class Produs(models.Model):
    category = models.ForeignKey(Category, related_name='produs', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produs_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    produse = ProductManager()
    

    class categorie(models.TextChoices):
        produs1 = "Masini tuns", "masinituns"
        produs2 = "Masini contur", "masinicontur"
        produs3 = "Shavere", "shavere"
        produs4 = "Foarfece", "foarfece"
        produs5 = "Accesorii", "accesorii"

    categorie = models.CharField(max_length=50, choices=categorie.choices)

    class vizitate(models.TextChoices):
        produs4 = "Cel mai vizitat", "celmaivizitat"

    vizitate = models.CharField(max_length=50, choices=vizitate.choices, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Produse'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:produs_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Cart(models.Model) :
    utilizator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_creator')
    cart = models.ForeignKey(Produs, on_delete=models.CASCADE)
    quantity=models.IntegerField()


class Comanda(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    adress = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, null=False, unique=True, blank=True)


    def get_absolute_url(self):
        return reverse('', args=[self.slug])

    def get_absolute_url(self):
        return reverse('store:comanda', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

