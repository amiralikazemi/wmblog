from django.db import models
from django.contrib.auth.models import User
from datetime import date , datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=225)
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
    	return self.title + ' | by : ' + str(self.author)