from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from scraper import buscador_producto, comparar

# Create your views here.


class Producto(object):
    def __init__(self, nombre,precio,url,imag):
        self.nombre=nombre
        self.precio=precio
        self.url=url
        self.imag=imag


def home(request):
    return render(request, 'home.html')


def buscar_producto(request):
    return render(request, 'buscar-producto.html')


def busqueda_producto(request):
    producto = request.POST['txt-producto']
    # lista_a=[['sebas','202','algo'],['ana','21','ld']]
    
    
    # return render(request,'listado-producto.html',{'productos':lista_a})

    try:
        lista_productos = buscador_producto.realizar_busqueda(producto)        
        lista_final = []
        lista_filtrada = comparar.filtrar_datos(lista_productos,producto)

        if len(lista_productos):
            for prod in lista_filtrada:
                p=Producto(prod[0],prod[1],prod[2],prod[3])
                lista_final.append(p)
            return render(request,'listado-producto.html', {'productos':lista_final, 'cantidad':len(lista_final)})    
        else:
            print('nada')
            return render(request,'listado-producto.html',{'cantidad':len(lista_productos)})
        

    except:
        print('An exception occurred')

def busqueda_varios_productos(request):
    lista_request = []
    lista_productos_encontrados = []
    lista_post=[]
    producto_post = ''
    
    for i in range(1,15):
        elemento_post='producto-'
        elemento_post+=str(i)
        lista_post.append(elemento_post)
    
    for elemento in lista_post:
        producto_post = request.POST[elemento]
        lista_request.append(producto_post)

    # producto_1 = request.POST['producto-1']
    # lista_request.append(producto_1)
    # producto_2 = request.POST['producto-2']
    # lista_request.append(producto_2)
    # producto_3 = request.POST['producto-3']
    # lista_request.append(producto_3)
    # producto_4 = request.POST['producto-4']
    # lista_request.append(producto_4)
    # producto_5 = request.POST['producto-5']
    # lista_request.append(producto_5)

    for producto in lista_request:
        if len(producto):
            lista_producto = buscador_producto.realizar_busqueda(producto)
            lista_filtrada = comparar.filtrar_datos(lista_producto,producto)
            
            if len(lista_producto):
                for prod in lista_filtrada:
                    p = Producto(prod[0],prod[1],prod[2],prod[3])
                    lista_productos_encontrados.append(p)
    
    return render(request,'listado-producto.html', {'productos':lista_productos_encontrados,'cantidad':len(lista_productos_encontrados)})    

def envio_correo(request,):
    prod = Producto(request.POST['nombre'],request.POST['precio'],request.POST['url'],'')
    return render(request,'formulario-mail.html',{'producto':prod})

def contacto(request):
    subject = request.POST['asunto']
    mensaje = request.POST['mensaje']+' '+request.POST['email']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.POST['email']]
    send_mail(subject,mensaje,email_from,recipient_list)
    return render(request, 'gracias.html')