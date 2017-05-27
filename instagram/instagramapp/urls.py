from django.conf.urls import url

from . import views

urlpatterns=[

      url(r'^Instagram/$', views.registro, name='registro'),
      url(r'^Crear_usuario/$', views.crear_usuario, name='crear_usuario'),
      url(r'^Pagina_inicio/$', views.inicio, name='inicio'),
      url(r'/Instagram/inicio_sesion/$', views.inicio, name='inicio')

]
