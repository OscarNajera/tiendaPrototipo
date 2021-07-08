from django.shortcuts import render,HttpResponse
from appPlantillas.models import Usuario ,Eventos

# Create your views here.
def saludo( request ):
    return HttpResponse( "Saludos  mundo "  )


def index( request ):
    EventoX   =Eventos.objects.all()
    return render(request, 'index.html',{'eventos':EventoX}   )

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

def GuardarUsuario(request):
    if request.method == 'GET':
        nombrex     = request.GET['nombre']
        apellidox   = request.GET['apellido']
        apodox      = request.GET['apodo']
        correox     = request.GET['correo']
        contrasenax = request.GET['contrasena']
        rfcx        = request.GET['rfc']
        if request.GET['publico'] == "x":
            publicox= True
        if request.GET['publico'] == "y":
            publicox= False
        
        xusuariox   =Usuario(
            nombre   = nombrex,
            apellido = apellidox,
            apodo    = apodox,
            correo   = correox,
            contrasena =contrasenax,
            rfc      = rfcx,
            publico= publicox,
    
        )    
        xusuariox.save()
        return HttpResponse(f"""Guardado EL usuario  
                                <a href="/">inicio</a> """  )

    else:
        return  HttpResponse("<h1>No se a podido guardar </h1>")  


#CReacion del evento que se guardara en la base
def CrearEvento(request):
    
     return render(request, 'CrearEvento.html'   )
    


def GuardarEvento(request):
    if request.method == 'POST':
        EventoX   =Eventos()
        EventoX.nombreEvento= request.POST.get('nombre')
        EventoX.fechaI      = request.POST.get('fechaI') 
        EventoX.fechaF      = request.POST.get('fechaF')
        EventoX.informacion = request.POST.get('informacion')
        EventoX.costo       = request.POST.get('costo')
        EventoX.horaInicio  = request.POST.get('horaInicio')
        EventoX.horafinal   = request.POST.get('horafinal')
        EventoX.lugar       = request.POST.get('lugar')
        EventoX.contacto    = request.POST.get('contacto')
        EventoX.redeSociales= request.POST.get('redeSociales')
        EventoX.imagen= request.FILES.get('imagen')

 
 
        EventoX.save()
        return HttpResponse(f"""Guardado EL Evento  
                                <a href="/">inicio</a> """  )

    else:
        return  HttpResponse("<h1>No se a podido guardar </h1>")  


def MostrarEventos(request):
    EventoX   =Eventos.objects.all()
     
    return render(request,"Eventos.html",{'eventos':EventoX}) 
    

def descripcion(request,xeve):
    
    Eventox = Eventos.objects.get(nombreEvento=xeve)
    
    return render(  request ,"descripcion.html",{"x":Eventox}   )
    










