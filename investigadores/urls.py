from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'investigadores.views.home', name='home'),
    # url(r'^investigadores/', include('investigadores.foo.urls')),
    url(r'^investigadores/',include('Publicaciones.urls')),
    # url(r'^investigadores/','Publicaciones.views.investigadores', name='lista_inv'),
    url(r'^$','Publicaciones.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
