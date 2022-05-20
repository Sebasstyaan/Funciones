"""Crear un diccionario de géneros literarios con el siguiente contenido:
Narrativa                   Dramático                       Lirico
La Vorágine                 El hechizo del agua         Los Heraldos negros
Don Quijote de la mancha    Primero es ella             Los versos del capitán
Con la soga al cuello       Hasta que salga el sol      Cantar de Mio Cid
Se debe mostrar la información organizada por categorías"""
print('-----------------------------------')

literario={
    'narrativa':['La Vorágine','Don Quijote de la mancha','Con la soga al cuello',],
    'Dramatico':['El hechizo del agua','Primero es ella','Hasta que salga el sol'],
    'Lirico': ['Los Heraldos negros','Los versos del capitán','Cantar de Mio Cid'],
}

print()
print('En el genero narrativo encontramos: '), print(literario['narrativa'])
print()
print('En el genero Dramatico encontramos: '), print(literario['Dramatico'])
print()
print('En el genero Lirico encontramos: '), print(literario['Lirico'])

def genero (literario):
    lit=input('digite')
    if lit in literario:
        for i in literario[lit]:
            print(i)
        
    else:
        print('No esta')

genero(literario)