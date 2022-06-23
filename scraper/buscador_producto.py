import string
from bs4 import BeautifulSoup
import requests


def obtener_BloquesProducto(elemento_html):
    bloque_producto = elemento_html.find_all(
        'li', {'class': 'ui-search-layout__item'})
    return bloque_producto


def obtener_descripcion_producto(bloque):
    bloque_desc = bloque.find(
        'h2', {'class': 'ui-search-item__title'}).getText()
    return bloque_desc


def obtener_precio_producto(bloque):
    bloque_precio = bloque.find(
        'span', {'class': 'price-tag-fraction'}).getText()
    return bloque_precio


def obtener_enlace_producto(bloque):
    enlace = bloque.find(
        'div', {'class': 'ui-search-result__image'}).find('a', href=True)['href']
    return enlace


def obtener_imagen_producto(bloque):
    imagen = bloque.find('img')['data-src']
    return(imagen)


def obtener_productos_recomendado(elemento_html):
    productos_recomendados = []
    bloque_producto = elemento_html.find_all(
        'li', {'class': 'ui-search-layout__item'})
    for bloque in bloque_producto:        
        prod = []
        descr = obtener_descripcion_producto(bloque)
        prod.append(descr)
        precio = obtener_precio_producto(bloque)
        traslator = str.maketrans('', '', string.punctuation)
        precio_numero = precio.translate(traslator)    
        prod.append(float(precio_numero))
        enlace = obtener_enlace_producto(bloque)
        prod.append(enlace)
        imagen = obtener_imagen_producto(bloque)
        prod.append(imagen)
        productos_recomendados.append(prod)
    return productos_recomendados


def realizar_busqueda(producto):
    url = 'https://listado.mercadolibre.com.ar/'
    producto = producto.replace(' ', '-')
    pagina = requests.get(url+producto)
    productos = []
    if pagina.status_code == 200:
        data = BeautifulSoup(pagina.content,'html.parser')
        productos = obtener_productos_recomendado(data)
    else:
        print('Pagina no Encontrada')
    return productos

