from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendario/$', views.CalendarioViewSet.as_view({'get': 'post'}), name='calendario'),
    url(r'^feriado/$', views.CalendarioferiadoViewSet.as_view({'get': 'post'}), name='feriado'),
]