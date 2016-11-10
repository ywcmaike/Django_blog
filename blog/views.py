from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogPost
# Create your views here.

def index(request):
    blog_list = BlogPost.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})
