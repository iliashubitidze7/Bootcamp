from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Product
from .models import Category
from .models import Comment
from .models import Order
from .models import OrderItem

# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(OrderItem)


