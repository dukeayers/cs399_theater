from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
# from django.contrib import admin
from views import home, events, movies, showtimes, store, team
urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^events', events),
    url(r'^movies', movies),
    url(r'^showtimes', showtimes),
    url(r'^store', store),
    url(r'^team', team),

    # url(r'^$', 'theater_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
