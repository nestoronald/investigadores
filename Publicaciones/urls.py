from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^todos/$', 'Miblog.views.articulos'),
    url(r'^todos/$','Publicaciones.views.investigadores'),
    url(r'^obtener/(?P<idinv>\d+)/$', 'Publicaciones.views.investigador'),
)