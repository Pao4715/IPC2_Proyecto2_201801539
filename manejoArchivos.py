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

def mostrarBuscar():
    global city
    print("Ingrese nombre de Ciudad: ")
    c = str(input('>'))
    city = listaD.buscar(c)
    print('Ciudad escogida: ' +  city.nombre)


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


