from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from .models import Profile
from django.views import View

from django.db import transaction
from .models import Order, OrderItem
# Create your views here.

@transaction.atomic
def create_order_and_items(order_data, items_data):
    order = Order.objects.create(**order_data)
    
    for i, item in enumerate(items_data):
        if i == 1:
            raise ValueError("Simulated exception!")  
        OrderItem.objects.create(order=order, **item)
    
    return order

def create_order_view(request):
    try:
        order_data = {'customer_name': 'Ilia shubitidze', 'total_price': 100}
        items_data = [{'product': 'Laptop', 'price': 50}, {'product': 'Mouse', 'price': 50}]
        
        create_order_and_items(order_data, items_data)
        return JsonResponse({"message": "Order created successfully!"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



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



    

