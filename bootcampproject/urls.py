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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import ProfileView
from core.views import PostListView
from core.views import ApiView
from core.views import HomeView
from core.views import ProductListCreate
from core.views import ProductRetrieveUpdateDestroy



schema_view = get_schema_view(
   openapi.Info(
      title="Product API",
      default_version='v1',
      description="API for managing products",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@productapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', ApiView.as_view()),
    path('blog/', PostListView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('api-auth', include('rest_framework.urls')),
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
