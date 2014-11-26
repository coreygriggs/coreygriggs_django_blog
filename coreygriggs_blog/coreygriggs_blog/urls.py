from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coreygriggs_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)
