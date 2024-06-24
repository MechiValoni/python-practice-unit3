from datos import *

def menu(): 
    return "\n1 - Ver Personaje\n2 - Árbol de Habilidades\n3 - Mejorar Habilidad\n4 - Salir"

#utilizar personaje creado en datos.py
while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    
    if opt == "1":
        print(personaje)
    elif opt == "2":
        a = sorted(habilidades, key=lambda h: h.nombre)
        print(*a, sep = "\n")
    elif opt == "3":
        habilidades_disponibles = [habilidad for habilidad in habilidades if not habilidad.maximo_alcanzado]
        for i,habilidad  in enumerate(habilidades_disponibles,1):
                print(f"{i}  {habilidad.nombre}")
        opt_h = int(input(f"Ingrese el numero de habilidad que desea dar 1 punto de los disponibles, puntos disponibles {personaje.cantidad_puntos_disponible} :"))
        personaje.mejorar_habilidad(habilidades_disponibles[opt_h-1])
        print(f"Se ha mejorado la habilidad de {personaje.nombre}")
    elif opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")