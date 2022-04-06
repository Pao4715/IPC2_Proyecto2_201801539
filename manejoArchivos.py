from calendar import c
import xml.etree.ElementTree as ET

from listaDoble import ListaDoble
from fila import Fila
from unidadM import UnidadM
from ciudad import Ciudad
from robot import Robot

import os

listaD = ListaDoble()
listaR = ListaDoble()
city = ''
entradas = []
unidades = []

def extraerDatos():

    print('Ingrese ruta del archivo xml')
    archivo = str(input('>>'))
    xmldoc = ET.parse(archivo)

    rect = {}
    nombre = ''
    noFilas = 0
    numero = 0
    columnas = 0

    raiz = xmldoc.getroot()

    for ciudad in raiz.iter('ciudad'):

        for n in ciudad.iter('nombre'):
            noFilas = n.get('filas')
            columnas = n.get('columnas')

            rect['nombre'] = n.text
            nombre = rect['nombre']

            #print(' #f: '+ noFilas + ' c: ' + columnas + ' n: ' + nombre)
            nuevaCiudad = Ciudad()
            nuevaCiudad.nombre = nombre
            nuevaCiudad.noFilas = noFilas
            nuevaCiudad.columnas = columnas

            for f in ciudad.iter('fila'):
                numero = f.get('numero')

                rect['fila'] = f.text
                secuencia = rect['fila']

                #print('fila numero =  ' + numero + '  secuencia: ' + secuencia)
                nuevaFila = Fila(numero, secuencia)
                nuevaCiudad.filas.insertarNodo(nuevaFila)

            for u in ciudad.iter('unidadMilitar'):
                fila = u.get('fila')
                columna = u.get('columna')

                rect['unidadMilitar'] = u.text
                capacidad = rect['unidadMilitar']

                #print('fila numero =  ' + fila + '  columna numero: ' + columna + '  Unidad:  ' + capacidad)
                nuevaUnidad = UnidadM(fila, columna, capacidad)
                nuevaCiudad.unidadesM.insertarNodo(nuevaUnidad)

            listaD.insertarNodo(nuevaCiudad)


    for robot in raiz.iter('robot'):

        for n in robot.iter('nombre'):
            tipo = n.get('tipo')
            capacidadR = n.get('capacidad')

            rect['nombre'] = n.text
            nombreR = rect['nombre']

            nuevoRobot = Robot(nombreR, tipo, capacidadR)
            listaR.insertarNodo(nuevoRobot)
    print('--------------------Ciudades--------------------------')
    listaD.recorrer()
    print('---------------------Robots---------------------------')
    listaR.recorrer()
    print('-----------------------------------------------------')


def mostrarBuscar():
    global city
    print("Ingrese nombre de Ciudad: ")
    c = str(input('>'))
    city = listaD.buscar(c)
    print('-----------------------------------------------------')
    print('Ciudad escogida: ' +  city.nombre)
    print('-----------------------------------------------------')
    encontrarEntradas()
    encontrarUCs()


def encontrarEntradas():
    global city 
    auxiliar = city.filas.primero
    while auxiliar != None:
        contador = 0
        for x in auxiliar.Node.secuencia:
            if x == 'E':
                entradas.append({'fila':  auxiliar.Node.numero , 'columna': contador})
            contador += 1
        auxiliar = auxiliar.siguiente


def encontrarUCs():
    global city 
    auxiliar = city.filas.primero
    while auxiliar != None:
        contador = 0
        for x in auxiliar.Node.secuencia:
            if x == 'C':
                unidades.append({'fila':  auxiliar.Node.numero , 'columna': contador})
            contador += 1
        auxiliar = auxiliar.siguiente


def buscarCamino():
    global entradas
    global unidades
    global city 
    auxiliar = city.filas.primero

    print('Entradas Disponibles: ' + str(entradas))
    print('Unidades Civiles Disponibles: ' + str(unidades))


def verificarRescue():
    estado = False
    while estado == False:
        print('------------------------------------------')
        print('Ingrese nombre de Robot a Utilizar: ')
        r = str(input('>'))
        robot = listaR.buscar(r)

        if robot:

            if robot.tipo == 'ChapinRescue':
                print('-------------------------------------------------------------')
                print('Robot escogido: ' + robot.nombre + ', ' + '  Capacidad: ' + str(robot.capacidad))
                print('-------------------------------------------------------------')
                estado = True
                return robot
            else:
                print('Robot no compatible para la misión')
                estado = False
        else:
            print('Robot no encontrado')
            estado = False


def encontrarUC():
    global unidades

    print('Ingrese Fila y columna de la Unidad Civil a Rescatar: ')
    fila = int(input('Fila: '))
    columna = int(input('Columna: '))

    for x in unidades:

        if int(x['fila']) == fila and int(x['columna']) == columna:

            print('-------------------------------------------------------------')
            print('Unidad Civil encontrada en ' + '\n Fila: ' + str(fila) + '\n Columna: ' + str(columna))
            print('-------------------------------------------------------------')
            return x

        else:
            print('Unidad Civil no encontrada')



def mision():
    global unidades
    print('------------Misión a Realizar-------------')
    print('1.- Mision de Rescate ') 
    print('2.- Mision de Extraccion de Recursos ') 
    print('------------------------------------------')
    mision = str(input('>'))

    if mision == '1':
        verificarRescue()
        encontrarUC()


def graficar():
    global city
    auxiliar = city.filas.primero
    auxiliar2 = city.unidadesM.primero
    cadena = ''
    file = open('Grafica.dot', 'w')
    cadena = cadena + 'digraph G { bgcolor="pink"\n'
    cadena = cadena + 'fontname="Helvetica,Arial,sans-serif" \n'
    cadena = cadena + 'node [fontname="Helvetica,Arial,sans-serif"] \n'
    cadena = cadena + 'edge [fontname="Helvetica,Arial,sans-serif"] \n'
    cadena = cadena + 'a0 [shape = "none", label=< \n'
    cadena = cadena + '<TABLE border="2" cellspacing="2" cellpadding="10" bgcolor="mediumpurple1"> \n'


    for i in range(int(city.noFilas)):

        cadena = cadena + '<TR> \n'

        for j in range(int(city.columnas)+1):

            if auxiliar is not None:

                if auxiliar2 is not None and int(auxiliar2.Node.fila)-1 == i and int(auxiliar2.Node.columna) == j:

                    cadena = cadena + '<TD border="1"  bgcolor="red"  gradientangle="270">'+ '</TD>\n'
                    auxiliar2 = auxiliar2.siguiente

                else:

                    if auxiliar.Node.secuencia[j] == '*':
                        cadena = cadena + '<TD border="1"  bgcolor="black"  gradientangle="270">'+ '</TD>\n'
                    elif auxiliar.Node.secuencia[j] == ' ':
                        cadena = cadena + '<TD border="1"  bgcolor="white"  gradientangle="270">'+ '</TD>\n'
                    elif auxiliar.Node.secuencia[j] == 'E':
                        cadena = cadena + '<TD border="1"  bgcolor="green"  gradientangle="270">'+ '</TD>\n'
                    elif auxiliar.Node.secuencia[j] == 'C':
                        cadena = cadena + '<TD border="1"  bgcolor="blue"  gradientangle="270">'+ '</TD>\n'
                    elif auxiliar.Node.secuencia[j] == 'R':
                        cadena = cadena + '<TD border="1"  bgcolor="gray"  gradientangle="270">'+ '</TD>\n'

        cadena = cadena + '</TR>\n'
        auxiliar = auxiliar.siguiente


    cadena = cadena + '</TABLE>>];\n'
    cadena = cadena + '}\n'
    file.write(cadena)
    file.close()
    os.system('dot -Tpng Grafica.dot -o Grafica.png')
    os.startfile(os.path.normpath('Grafica.png'))


