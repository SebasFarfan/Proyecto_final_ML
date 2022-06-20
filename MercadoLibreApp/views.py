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

def busqueda_varios_productos(request):
    lista_request = []
    lista_productos_encontrados = []

    producto_1 = request.POST['producto-1']
    lista_request.append(producto_1)
    producto_2 = request.POST['producto-2']
    lista_request.append(producto_2)
    producto_3 = request.POST['producto-3']
    lista_request.append(producto_3)
    producto_4 = request.POST['producto-4']
    lista_request.append(producto_4)
    producto_5 = request.POST['producto-5']
    lista_request.append(producto_5)

    for producto in lista_request:
        if len(producto):
            lista_producto = buscador_producto.realizar_busqueda(producto)
            if len(lista_producto):
                for prod in lista_producto:
                    p = Producto(prod[0],prod[1],prod[2],prod[3])
                    lista_productos_encontrados.append(p)
    
    return render(request,'listado-producto.html', {'productos':lista_productos_encontrados})    
