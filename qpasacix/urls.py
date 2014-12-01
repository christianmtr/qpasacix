from django.conf.urls import patterns, include, url
from django.contrib import admin
from fotos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qpasacix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^albumes/', views.obtienealbumes, name='obtienealbumes'),

	url(r'^album/(\d+)/', views.muestraalbum, name='muestraalbum'),    
)
