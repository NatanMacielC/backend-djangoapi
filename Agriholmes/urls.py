"""Agriholmes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from empresas.api import viewsets as empresasviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from fullcalendar import views as calendarviewsets
from parametrização import views as parameterviewsets

route = routers.DefaultRouter()

route.register(r'empresas', empresasviewsets.EmpresasViewSet, basename="Empresas")
route.register(r'calendar', calendarviewsets.CalendarViewSet, basename="Calendario")
route.register(r'feriado', calendarviewsets.FeriadoViewSet, basename="Feriado")
route.register(r'evento', parameterviewsets.EventoViewSet, basename="Evento")
route.register(r'regras', parameterviewsets.RegrasViewSet, basename="Regras")


urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # home
    path('', include(route.urls)),
    # authentication
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path(r'^', include('fullcalendar.urls')),
    path(r'^', include('parametrização.urls')),
]