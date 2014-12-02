from django.shortcuts import render, get_object_or_404
from .models import Post
from django.template import RequestContext

# Create your views here.

def index(request):
	return render(request, 'blog/index.html', context_instance=RequestContext(request))

def blog(request):
	posts = Post.objects.filter(published=True)
	return render(request, 'blog/blog.html', {'posts': posts}, context_instance=RequestContext(request))

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post': post})

def contact(request):
	return render(request, 'blog/contact.html')