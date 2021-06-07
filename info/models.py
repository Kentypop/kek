from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Company(models.Model):
	name= models.CharField(max_length=50)
	url= models.URLField(max_length=100)
	creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class servicehair(models.Model):
	name= models.CharField(max_length=50)
	price= models.DecimalField(max_digits= 5, decimal_places=2)