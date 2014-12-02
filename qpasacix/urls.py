from django.conf.urls import patterns, include, url
from django.contrib import admin
from fotos import views as fotos
from index import views as inicio

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qpasacix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

	url(r'^albumes/', fotos.obtienealbumes, name='obtienealbumes'),

	url(r'^album/(\d+)/', fotos.muestraalbum, name='muestraalbum'),

	url(r'^index/', inicio.inicio, name='inicio'),

	url(r'^comparte/', inicio.compartir, name='compartir'),
)
