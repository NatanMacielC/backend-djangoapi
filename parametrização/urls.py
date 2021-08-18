from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regras/$', views.EventoViewSet.as_view({'get': 'post'}), name='Eventos'),
    url(r'^eventos/$', views.RegrasViewSet.as_view({'get': 'post'}), name='Regras'),
]