from django.shortcuts import render,HttpResponse
from appPlantillas.models import Usuario

# Create your views here.
def saludo( request ):
    return HttpResponse( "Saludos  mundo "  )


def index( request ):
    return render(request, 'index.html'   )

def NuevosEventos( request ):
    return render(request, 'NuevosEventos.html'   )

def registro( request ):
    return render(request, 'registro.html'   )


def CrearUsuario(request):
    xusuario=Usuario(
        nombre   = "Primer Usuario",
        apellido = "X Apeellido",
        apodo  = "Fulanito de tal",
        correo   = "fulanito@flnto.com",
        contrasena ="123456",
        rfc = "XXX111YYY",
        publico= True,
    
    )
    xusuario.save()
    return HttpResponse(f"Usuario Agregado"+xusuario.nombre)
















