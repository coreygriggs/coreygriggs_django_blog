from django.shortcuts import render, get_object_or_404
from .models import Post, Headline
from django.template import RequestContext


def index(request):
	posts = Post.objects.filter(published=True).all()[:3]
	headline = get_object_or_404(Headline)
	return render(request, 'blog/index.html', {'headline': headline, 'posts': posts}, context_instance=RequestContext(request))


def blog(request):
	posts = Post.objects.filter(published=True)
	return render(request, 'blog/blog.html', {'posts': posts}, context_instance=RequestContext(request))


def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post': post})


def contact(request):
	return render(request, 'blog/contact.html')