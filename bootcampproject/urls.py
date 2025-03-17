"""
URL configuration for bootcampproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from core.views import ProfileView
from core.views import PostListView
from core.views import ApiView
from core.views import HomeView
from core.views import create_order_view
from core.views import ProductListCreate
from core.views import ProductRetrieveUpdateDestroy

from rest_framework import routers
from core import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', ApiView.as_view()),
    path('blog/', PostListView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('create-order/', create_order_view, name='create-order'),
    path('api-auth', include('rest_framework.urls')),
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]
