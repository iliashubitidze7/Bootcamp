from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Product, Post, Profile
from .permissions import IsManager
from .tasks import send_welcome_email
import pytest



# Create your views here.

def trigger_task(request):
    user_id = 3  
    send_welcome_email.apply_async(args=[user_id])
    return JsonResponse({"message": "Task triggered successfully"})


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsManager]



class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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

    response = client.get('/products/')
    assert response.status_code == status.HTTP_200_OK

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

    response = client.get(f'/products/{product.pk}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Product 1'

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

