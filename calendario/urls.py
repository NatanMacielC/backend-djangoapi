from django.conf.urls import url
from . import viewsets

urlpatterns = [
    url(r'^calendario/$', viewsets.CalendarioViewSet.as_view({'get': 'post'}), name='calendario'),
    url(r'^feriado/$', viewsets.CalendarioferiadoViewSet.as_view({'get': 'post'}), name='feriado'),
]