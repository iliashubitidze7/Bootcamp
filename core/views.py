from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db import transaction
from rest_framework import generics
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Order, OrderItem , Product, Post, Profile
from .permissions import IsManager
import pytest


# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsManager]



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


@pytest.mark.django_db
def test_product_list_create():
    client = APIClient()

    # Test GET (List Products)
    response = client.get('/products/')
    assert response.status_code == status.HTTP_200_OK

    # Test POST (Create Product)
    product_data = {
        'name': 'Product 1',
        'price': 100.00,
        'description': 'A great product'
    }
    response = client.post('/products/', product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Product 1'

@pytest.mark.django_db
def test_product_retrieve_update_destroy():
    client = APIClient()
    product = Product.objects.create(name='Product 1', price=100.00, description='A great product')

    # Test GET (Retrieve Product)
    response = client.get(f'/products/{product.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Product 1'

    # Test PUT (Update Product)
    updated_data = {
        'name': 'Updated Product',
        'price': 120.00,
        'description': 'Updated description'
    }
    response = client.put(f'/products/{product.pk}/', updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Updated Product'

    # Test DELETE (Delete Product)
    response = client.delete(f'/products/{product.pk}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

