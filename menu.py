from manejoArchivos import extraerDatos, graficar, mostrarBuscar

class Menu:

    def menuPrincipal():
        print("=================================")
        print("           MENÚ PRINCIPAL          ")
        print("=================================")
        print("1. Cargar Archivo                  ")
        print("2. Escoger Ciudad                  ")
        print("3. Mostrar Ciudad                  ")
        print("4. Iniciar Misiones                ")
        print("5. Reporte de Misión               ")
        print("6. Salir                           ")
        print("=================================")


    while True:
        menuPrincipal()
        opcion = input("Escoja una opción >> ") 

        if opcion == "1":
            extraerDatos()
        elif opcion == "2":
            mostrarBuscar()
        elif opcion == "3":
            graficar()
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            break
        else: 
            input("Selección no válida")
