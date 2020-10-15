from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from .models import Post
# Create your views here.

class HomeView(ListView):
	model = Post
	template_name = 'blog/home.html'
	ordering = ['-post_date']