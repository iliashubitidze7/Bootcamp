from django.db import models

import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    name = models.CharField(max_length=250, default ='ilia')
    lastname = models.CharField(max_length=250, default ='shubitidze')
    age = models.IntegerField(default=28)
    job = models.CharField(max_length=250, default= 'beck-end Developer')
    date_of_birth = models.DateField(default=datetime.date(1996, 10, 30))

    def __str__(self):
        return f"{self.name} {self.lastname} , Age: {self.age}, Job: {self.job}, DOB: {self.date_of_birth}"


