from django.shortcuts import render
from blog.models import Post

def landing_page(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    return render(request, 'about.html', {'posts': posts})

def about_page(request):
    return render(request, 'about.html')

