"""Diseñe una aplicacionque, dada una lista de 10 elementos, realice las siguientes acciones:
*Recorrer la lista y mostrar el contenido de la lista
*Hacer una funcion recorra la lista y devuelva una cadena con los valores de la lista
*Ordenar de mayor a menor
*Buscar un elemento que el usuario pida por teclado
*Mostrar su tamaño o longitud"""
from logging.config import valid_ident
import random

def mostrasCadena(lista):
    cadena=""
    for i in range(len(lista)):
        cadena += str(lista[i]) + ', '
    return cadena

tamaño=10

lista=[0]*tamaño
for i in range(tamaño):
    lista[i] = random.randint(0,50)

print('Esta es la lista: ')
print(lista)

print()
print('Esta es la lista como cadena: ')
print(mostrasCadena(lista))

lista.sort(reverse=True)
print('Esta es la lista ordenada de mayor a menor: ')
print(lista)

print()
elemento = int(input('Ingrese un valor a buscar: '))

if elemento in lista:
    print('El numero se encuentra en la lista')
    print('En la posicion: ') 
    print (lista.index(elemento))
else:
    print('El numero no se encuentra en la lista')

print()
print('El tamaño de la lista es: {}'.format(len(lista)))