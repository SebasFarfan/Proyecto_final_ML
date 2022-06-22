import string
import nltk


palabra='samgsung a02 2007'
print(palabra)
palabra= palabra.replace(' ','-')
print(palabra)

precio = '30.950'
print(precio)
traslator = str.maketrans('', '', string.punctuation)
no_puntuaction = precio.translate(traslator)    
# precio = string.punctuation(precio)
print(no_puntuaction)

palabra = 'analia'
palabra2= ''
palabra3= 'gr 4 '

listaa=[palabra,palabra2,palabra3]
print(listaa)
print('longitud palabra 2:',len(palabra2))
# palabra11 = str.split(palabra3)
# print('longitud palabra 11:',len(palabra11))

class Producto(object):
    def __init__(self, nombre,precio,url,imag):
        self.nombre=nombre
        self.precio=precio
        self.url=url
        self.imag=imag

lista111 = []
p1 = Producto('sebastian','123','hhtt://djdj/aas','imagen3')
lista111.append(p1)
p2 = Producto('analia','098','hhtt://djdj/aas','imagen3')
lista111.append(p2)


lista_ejemplo = ['1','2']
print(len(lista_ejemplo))
for i in range(len(lista_ejemplo)):
    print(i)