from django.shortcuts import render, get_object_or_404
from .models import Post, Headline
from .forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def index(request):
	posts = Post.objects.filter(published=True).all()[:3]
	if len(posts) > 0:
		headline = get_object_or_404(Headline)
		return render(request, 'blog/index.html', {'headline': headline, 'posts': posts}, context_instance=RequestContext(request))
	else:
		return render(request, 'blog/index.html')


def blog(request):
	posts = Post.objects.filter(published=True)
	return render(request, 'blog/blog.html', {'posts': posts}, context_instance=RequestContext(request))


def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post': post})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			send_mail(
				data['subject'],
			    data['message'],
			    data.get('email', 'noreply@example.com'),
			    ['siteowner@example.com'],

			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I want to hire you!'}
		)
	return render(request, 'blog/contact.html', {'form': form})