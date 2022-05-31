"""Realizar un algoritmo que permita registrar y mostrar la información de 5 estudiantes de un 
colegio Además de contar con un menú con las siguientes opciones: 
a. Ingresar estudiantes
b. Listar estudiantes
c. Modificar notas de un estudiante por código
d. Consultar la nota definitiva de un estudiante por código
e. Salir"""

def leerMenu():
    print("""Escoja la opcion que va a realizar\n
        a: Ingresar Estudiantes 
        b: Ver La Lista De Estudiantes
        c: Modificar Las Notas Del Estudiante 
        d: Consultar Nota Definitiva Del Estudiante 
        e: Salir""")
    opc=input('Introduzca opcion que desea consultar: ')
    opc = opc.lower()
    return opc

def IngresarEstudiante():
    estu={
        'nombre' : '',
        'codigo' : 0,
        'notas' : []
    }
    print('Ingresando estudiantes')
    estu['nombre'] =input('Nombre del estudiante: ')
    estu['codigo'] =input('id del estudiante: ')
    while True:
        nota=int(input('Ingrese una nota: (-1 para terminar): '))
        if nota <0:
            break
        estu['notas'].append(nota)
    return estu



def ListarEstudiantes():
    print('Listando estudiantes')
    for j in listaEstudiantes:
        print('codigo: {}  nombre: {}'.format(j['codigo'], j['nombre']))


def ModoficarNotas():
    global listaEstudiantes
    print('Modificando Notas')
    codigo = input('Digite el id del estudiante: ')
    for k in range(len(listaEstudiantes)):
        if listaEstudiantes[k]['codigo'] == codigo:
            for n in range(len(listaEstudiantes[k]['notas'])):
                nota=input('Nota Actual: {}. nueva nota? '.format(listaEstudiantes[k]['notas'][n]))
                try:
                    val=int(nota)
                    listaEstudiantes[k]['notas'][n]=val
                except:
                    continue
        else:
            print('Id No Existe')

def ConsultarNotas():
    #print('Consultando Notas')
    global listaEstudiantes
    codigo = input('Digite el id del estudiante: ')
    for c in range(len(listaEstudiantes)):
        if listaEstudiantes[c]['codigo'] == codigo:
            promedio=0
            for g in range(len(listaEstudiantes[c]['notas'])):
                promedio += listaEstudiantes[c]['notas'][g]

            promedio = promedio / len(listaEstudiantes[c]['notas'])

            print('Promedio de la nota final es: {}'.format(promedio))

#Programa Principal +++++++++++++++++++++++++++++++++++


listaEstudiantes = []

while True:
    print('--------------------------------')
    opc = leerMenu()
    if opc == 'a':
        listaEstudiantes.append(IngresarEstudiante())
    elif opc == 'b':
        ListarEstudiantes()
    elif opc == 'c':
        ModoficarNotas()
    elif opc == 'd':
        ConsultarNotas()
    elif opc == 'e':
        break

print(listaEstudiantes)