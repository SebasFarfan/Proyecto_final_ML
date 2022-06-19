from django.shortcuts import render

from scraper import buscador_producto

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
        if len(lista_productos):
            for prod in lista_productos:
                p=Producto(prod[0],prod[1],prod[2],prod[3])
                lista_final.append(p)
            return render(request,'listado-producto.html', {'productos':lista_final})    
        else:
            print('nada')
            return render(request,'listado-producto.html')
        

    except:
        print('An exception occurred')
