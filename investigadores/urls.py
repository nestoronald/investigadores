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
    url(r'^login/$', 'Publicaciones.views.login_view', name="vista_login"),
    url(r'^logout/$', 'Publicaciones.views.logout_view', name="vista_logout"),
    url(r'^registro/$','Publicaciones.views.register_view',name='vista_registro'),
    url(r'^editPerfil/(?P<id_user>.*)/$','Publicaciones.views.edit_profile',name= "view_editar_perfil"),
    url(r'^editarPerfil/$','Publicaciones.views.editar_perfil',name= "editar_perfil"),
    url(r'^lista/$','Publicaciones.views.publication_list',name= "editar_perfil"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
