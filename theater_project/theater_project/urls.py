from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home
urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    # url(r'^$', 'theater_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
