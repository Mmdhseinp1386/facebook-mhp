from django.urls import path
from core.views import say_hello

urlpatterns = [
    path('harchi/', say_hello),
]