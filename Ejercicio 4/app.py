from datos import *

def buscar_estadia(patente:str) -> Estadia:
    for estadia in estadias:
        if estadia.patente == patente:
            return estadia
    return None

while True:

    print('''1. Ingresar Estadia
2. Finalizar Estadia
3. Ver estadias
4. Salir''')
    opt = int(input("Ingresar una opción... "))

    if opt == 1:
        pat = input("Ingrese la patente: ")
        estadias.append(Estadia(pat))
        print("Estadia ingresada correctamente... ")
    elif opt == 2:
        pat = input("Ingrese la patente: ")
        estadia_encontrada = buscar_estadia(pat)
        if(estadia_encontrada):
            print(f"MONTO A ABONAR: {estadia_encontrada.registrar_salida()}")
            continue
        print("Estadia no encontrada... ")
    elif opt == 3:
        for estadia in estadias:
            print(estadia)
    elif opt == 4:
        print("Hasta Luego!.")
        break