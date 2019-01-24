from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.

def blogs(request):
    blogs = Blog.objects.order_by("pub_date").reverse()
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
