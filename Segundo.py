""" Diseñe un algoritmo que defina una lista vacia y luego le agregue valores a la lista, teniendo
en cuenta que su longitud debe ser menor a la digita por el usuario.
"""
print('-----------------------------------')
lista2=[]
longitud = int(input('Digite el tamaño de su lista: '))
longitud = longitud-1
i = 0
while i != longitud:
    usuario = int(input('Digite valor para su lista: '))
    i += 1
    lista2.append(usuario)
print(lista2)