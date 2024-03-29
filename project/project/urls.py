from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from apps.home.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)