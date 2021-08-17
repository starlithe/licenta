from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'appointment'

urlpatterns = [
    path('create-appointment/', views.create_appointment, name='create_appointment'),
    path('detail-appointment/<str:slug>/', views.view_detail_appointment, name='view_detail_appointment'),
    path('unchecked-appointments/', views.view_unchecked_appointment, name='view_unchecked_appointment'),
    path('checked-appointments/', views.view_checked_appointment, name='view_checked_appointment'),
]