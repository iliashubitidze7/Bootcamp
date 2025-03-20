from django.db import models
from django.db import transaction

import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    desciption = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 

    def __str__(self):
        return f"Comment on {self.post.title}"
    

class Profile(models.Model):
    name = models.CharField(max_length=250, default ='ilia')
    lastname = models.CharField(max_length=250, default ='shubitidze')
    age = models.IntegerField(default=28)
    job = models.CharField(max_length=250, default= 'beck-end Developer')
    date_of_birth = models.DateField(default=datetime.date(1996, 10, 30))

    def __str__(self):
        return f"{self.name} {self.lastname} , Age: {self.age}, Job: {self.job}, DOB: {self.date_of_birth}"


class Category(models.Model):
    name = models.CharField(max_length=100, default= 'Soft Drinks', db_index=True)
    desctiption = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desctiption = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
