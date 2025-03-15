from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from .models import Profile
from django.views import View

# Create your views here.

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



    

