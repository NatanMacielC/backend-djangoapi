from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendario/$', views.CalendarViewSet.as_view({'get': 'post'}), name='calendario'),
    url(r'^feriado/$', views.FeriadoViewSet.as_view({'get': 'post'}), name='feriado'),
]