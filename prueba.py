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
