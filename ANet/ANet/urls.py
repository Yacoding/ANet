from django.conf.urls import patterns, include, url
import ANet
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ANet.views.home', name='home'),
    # url(r'^ANet/', include('ANet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_medias/(?P<path>.*)$','django.views.static.serve',{'document_root':ANet.settings.STATICFILES_DIRS, 'show_indexes': True}),
    url(r'^register/$', 'blog.views.register'),
    url(r'^blog/$', 'blog.views.blog'),
    url(r'^userinfo/$', 'blog.views.userinfo'),
    url(r'^logout/$', 'blog.views.logout'),
    url(r'^blog/view/(?P<slug>[^\.]+).html','blog.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),
)
