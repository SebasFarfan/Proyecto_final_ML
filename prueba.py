import string

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
