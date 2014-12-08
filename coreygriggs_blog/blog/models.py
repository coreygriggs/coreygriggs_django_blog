from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])


class Headline(models.Model):
    headline = models.CharField(max_length=255)
    is_current = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.headline


class ContactFormRequests(models.Model):
    email = models.EmailField(max_length=100, unique=False)
    subject = models.CharField(max_length=200, unique=False)
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500, unique=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.subject