from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fisco/$', views.FiscoViewSet.as_view({'get': 'post'}), name='Fisco'),

]