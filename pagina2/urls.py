"""pagina2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from appPlantillas.views import saludo,index,NuevosEventos,registro,CrearUsuario,GuardarUsuario,CrearEvento,GuardarEvento,MostrarEventos,descripcion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', saludo, name="saludo"),    
    path('saludo/', saludo, name="saludo"),
    path('', index, name="index"),
    path('NuevosEventos/', NuevosEventos, name="NuevosEventos"),
    path('registro/', registro, name="registro"),
    path('CrearUsuario/', CrearUsuario, name="CrearUsuario"),
    path('GuardarUsuario/', GuardarUsuario, name="GuardarUsuario"),
    path('CrearEvento/', CrearEvento, name="CrearEvento"),
    path('GuardarEvento/', GuardarEvento, name="GuardarE"),
    path('MostrarEventos/', MostrarEventos, name="MostrarEve"),
    path('descripcion/<str:xeve>', descripcion, name="descripcion"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)