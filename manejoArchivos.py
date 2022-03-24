import xml.etree.ElementTree as ET
from listaDoble import ListaDoble


listaD = ListaDoble()

def extraerDatos():

    print('Ingrese ruta del archivo xml')
    archivo = str(input('>>'))
    xmldoc = ET.parse(archivo)

    rect = {}
    nombre = ''
    noFilas = 0
    filas = []
    numero = 0
    columnas = 0

    raiz = xmldoc.getroot()

    for ciudad in raiz.iter('ciudad'):
        
        for n in ciudad.iter('nombre'):
            noFilas = n.get('filas')
            columnas = n.get('columnas')

            rect['nombre'] = n.text
            nombre = rect['nombre']

            print(' #f: '+ noFilas + ' c: ' + columnas + ' n: ' + nombre)

            for f in ciudad.iter('fila'):
                numero = f.get('numero')

                rect['fila'] = f.text
                secuencia = rect['fila']

                print('fila numero =  ' + numero + '  secuencia: ' + secuencia)
            for u in ciudad.iter('unidadMilitar'):
                fila = u.get('fila')
                columna = u.get('columna')

                rect['unidadMilitar'] = u.text
                capacidad = rect['unidadMilitar']
                
                print('fila numero =  ' + fila + '  columna numero: ' + columna + '  Unidad:  ' + capacidad)


        

extraerDatos()
