from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^todos/$', 'Miblog.views.articulos'),
    url(r'^$','Publicaciones.views.investigadores'),
    url(r'^(?P<idinv>\d+)/$', 'Publicaciones.views.investigador'),
)