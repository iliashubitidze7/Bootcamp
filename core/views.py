from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db import transaction
from rest_framework import generics
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import ProductSerializer
from .models import Order, OrderItem , Product, Post, Profile

import pytest


# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@transaction.atomic
def create_order_and_items(order_data, items_data):
    order = Order.objects.create(**order_data)
    
    for item_data in items_data:
        OrderItem.objects.create(order=order, **item_data)
    

    if len(items_data) > 3:
        raise Exception("Simulating an error mid-transaction!")

order_data = {'customer_name': 'ilia', 'total_amount': 200.00}
items_data = [
    {'product_name': 'Product 1', 'quantity': 2},
    {'product_name': 'Product 2', 'quantity': 1},
    {'product_name': 'Product 3', 'quantity': 5},

]

try:
    create_order_and_items(order_data, items_data)
    print("Order and items created successfully.")
except Exception as e:
    print(f"Transaction failed: {e}")


class HomeView(View):
    def get(self, request):
        return HttpResponse('Hello, Django Bootcamp!')
        

class ApiView(View):
    def get(self, request):
        data = data = {
        "message": "Welcome to Django Bootcamp API!",
        "status": "success"
    }
        return JsonResponse(data)

class PostService:
    def get_all_posts(self):
        return Post.objects.all()

class ProfileService:
    def get_all_profiles(self):
        return Profile.objects.all()

class PostListView(View):
    def get(self, request):
        post_service = PostService()
        posts = post_service.get_all_posts()
        return render(request, 'core/post_list.html', {'posts': posts})


class ProfileView(View):
    def get(self, request):
        profile_service = ProfileService()
        profile = profile_service.get_all_profiles()
        return render (request, 'core/profile.html', {'profile': profile})



    

