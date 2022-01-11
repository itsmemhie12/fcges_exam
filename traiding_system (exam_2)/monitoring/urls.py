from django.contrib import admin
from django.urls import path
from monitoring import views

urlpatterns = [
    path('trade', views.trading, name='trading')
]
