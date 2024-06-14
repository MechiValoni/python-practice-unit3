from datos import *

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

def nueva_lista():
    print("Creando una lista de reproduccion ...")
    nombre = input("Ingrese el nombre de la lista: ")
    lista = ListaReproduccion(nombre)

    print("Seleccione al menos un video para crear la lista...")
    for i,video in enumerate(videos,1):
        print(f"{i} - {video.nombre}")

    index_video = int(input("Seleccione el video: "))
    v = videos[index_video-1]

    lista.add_video(v)
    listas.append(lista)

    print("Se creo la lista exitosamente...")

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        for video in sorted(videos, key=lambda x: x.nombre):
            print(video)
        continue
    if opt == "2":
        nueva_lista()
        continue
    if opt == "3":
        for lista in listas:
            if lista.videos:
                print(lista)
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")