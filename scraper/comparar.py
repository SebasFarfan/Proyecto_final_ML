from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import warnings

warnings.filterwarnings('ignore')

def find_similar(tfidfMatrix, indice, top_n=10):
    '''
    Método que busca documentos similares usando metodo de coseno de linear_kernel. \n
    en base a ese cálculo que se realiza se obtiene un valor que representa que tan parecido \n
    es un documento con respecto a una serie de documentos procesados.\n
    Arg: \n
    tfidfMatrix: [TfidfVectorizer] matriz TF-IDF \n
    indice: [int] posicion del docuento en un lista que se usa para comparar \n
    top_n: [int] cantidad de elementos o documentos a mostrar de un ranking de documentos \n
    que más se parecen.
    '''
    coseno_similares = linear_kernel(tfidfMatrix[indice:indice+1], tfidfMatrix).flatten()
    lista_indices = []
    for i in coseno_similares.argsort()[::-1]:
        if i != indice:
            lista_indices.append(i)
    
    related_doc_indices = lista_indices
    listado_indices_similares = []
    for indice in related_doc_indices[0:top_n]:
        listado_indices_similares.append((indice, coseno_similares[indice]))
    return listado_indices_similares

def obtener_datos(lista_datos,prod):
    diccionario_contenido = {}
    contador_archivos = 0
    for dato in lista_datos:
        dato_mi= dato.lower()        
        diccionario_contenido[contador_archivos]=dato_mi
        contador_archivos+=1
    prod_mi = prod.lower()
    diccionario_contenido[contador_archivos]=prod_mi
    return diccionario_contenido

def extraer_titulo(lista_completa):
    lista_limpia=[]
    for producto in lista_completa:
        lista_limpia.append(producto[0])
    return lista_limpia



def obtener_lista_productos(lista_prod,prod):        
    titulos = extraer_titulo(lista_prod)
    dic_conte=obtener_datos(titulos,prod)
    tfidf = TfidfVectorizer()
    # crea objeto de la matriz TF-IDF con los datos
    tfs = tfidf.fit_transform(dic_conte.values())
    # se convierte el diccionario en una lista
    lista_contenido = list(dic_conte.items())
    lista_similaress =[]
    for indice, score in find_similar(tfs, 0):
        # print(str(round(score,10)),lista_contenido[indice][0])
        # print('-'*100)
        if score>0.1 :
            lista_similaress.append(lista_contenido[indice][0])
    
    
    lista_definitiva=[]
    for i in range(len(lista_similaress)):
        if i >0:
            print(lista_contenido[lista_similaress[i]])
            lista_definitiva.append(lista_contenido[lista_similaress[i]])    
    return lista_definitiva

def lista_filtrada(lista_completa,prod):
    lista_definitiva = []
    lista_lim = obtener_lista_productos(lista_completa,prod)
    for producto in lista_completa:
        for titulo in lista_lim:

            if titulo[1]== producto[1].lower():
                lista_definitiva.append(producto)
                break
    
    return lista_definitiva

    
# lista_prodddd=[['Motorola G8 4ram','34444'],['Moto Edge','123'],['Motorola G7 ert','1234']]
# productito='motorola g8'
# print(lista_filtrada(lista_ro,produdctio))

def filtrar_datos(lista_productos,producto):

    lista_titulos=extraer_titulo(lista_productos)
    dic_conte=obtener_datos(lista_titulos,producto)
    print(type(dic_conte))
    print('--','diccionario de titulos','--')
    print(dic_conte)
    tfidf = TfidfVectorizer()
    # crea objeto de la matriz TF-IDF con los datos
    tfs = tfidf.fit_transform(dic_conte.values())
    # se convierte el diccionario en una lista
    lista_contenido = list(dic_conte.items())
    print('--','se convierte el diccionario en una lista','--')
    print(lista_contenido)
    # posicion a comparar. siempre a comparar con el ultimo elemento
    posicion = len(lista_contenido)-1
    print('ultimo elemento-->',lista_contenido[len(lista_contenido)-1])
    lista_similaress =[]
    for indice, score in find_similar(tfs, (len(lista_contenido)-1)):
            # print(str(round(score,10)),lista_contenido[indice][0])
            # print('-'*100)
            if score>0.1 :
                lista_similaress.append(lista_contenido[indice][0])
    print(lista_similaress)
    lista_definitiva=[]
    for i in range(len(lista_similaress)):
        # if i >0:
        print(lista_contenido[lista_similaress[i]])
        lista_definitiva.append(lista_contenido[lista_similaress[i]])

    print(lista_definitiva)
    # for i in range(len(lista_definitiva)):
    #     print(lista_definitiva[i][1])
    lista_definitivaff=[]

    for producto in lista_productos:
        for titulo in lista_definitiva:
            if titulo[1]== producto[0].lower():
                lista_definitivaff.append(producto)
                break
    # print(lista_definitivaff)
    return(lista_definitivaff)

# print(filtrar_datos(lista_prodddd,productito))
# lista_titulos = ['motorola g8','Moto E40 64 GB gris acero 4 GB RAM', 'Motorola Moto G8 Power Lite 64 Gb Azul Bueno',
#  'Motorola Moto G8 Plus Xt2019 64gb Refabricado Azul', 'Moto G60s 128 GB azul 6 GB RAM']
# diccionario_conte = obtener_datos(lista_titulos)
# tfidf = TfidfVectorizer()

# crea objeto de la matriz TF-IDF con los datos
# tfs = tfidf.fit_transform(diccionario_conte.values())

# se convierte el diccionario en una lista
# lista_contenido = list(diccionario_conte.items())

# lista_similaress =[]
# for indice, score in find_similar(tfs, 0):
#     print(str(round(score,10)),lista_contenido[indice][0])
#     print('-'*100)
#     if score>0.3 :
#         lista_similaress.append(lista_contenido[indice][0])

# print(lista_similaress)
# # print(lista_titulos[3])
# for valor in lista_similaress:
#     print(lista_titulos[valor])
    
# print('-'*50)
# print(filtrar_datos(lista_prodddd,productito))
