# FRONTEND
# Aca van todos los inputs y prints
from datos import *

def menu_admin():
    return '''1. Nuevo usuario
2. Buscar usuario
3. Buscar libro
7. Cerrar sesión'''

def menu_usuario():
    return '''4. Ver mis libros
5. Aregar libro a mi coleccion
6. Eliminar libro de mi coleccion
7. Cerrar sesión'''

def loggin(user_name, user_pass):
    for usuario in usuarios: 
        if usuario.validar_credenciales(user_name, user_pass):
            return usuario
    return None

def nuevo_usuario():
    user = input("Ingrese un nombre de usuario: ")
    passw = input("Ingrese una password de usuario: ")
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    anio = int(input("Ingrese el anio de nacimiento: "))
    mes = int(input("Ingrese el mes de nacimiento: "))
    dia = int(input("Ingrese el dia de nacimiento: "))
    for i, tipo_documento in enumerate(tipos_documento, 1):
        print(f"{i} {tipo_documento}")
    indice = int(input("Ingrese el tipo de documento.. ")) #no lo validamos
    admin = int(input("Ingrese 1 si es usuario administrador: ")) #no lo validamos
    admin = admin == 1
    nuevo_usuario = Usuario(user, passw, '', nombre, apellido, date(anio, mes, dia), 5, tipos_documento[indice-1], admin)
    usuarios.append(nuevo_usuario)

def buscar_usuario():
    user = input("Ingrese un nombre de usuario que desea buscar: ")
    for usuario in usuarios: 
        if usuario.get_user_name() == user:
            print(usuario)
            return
    print("Usuario no encontrado. ")

def buscar_libro():
    isbn = input("Ingrese un ISBN de libro a buscar.. ")
    libro_encontrado = None
    for libro in libros: 
        if libro.get_isbn() == isbn:
            libro_encontrado = libro
            break
    if(libro_encontrado):
        for usuario in usuarios:
            if libro_encontrado in usuario.get_libros():
                print(usuario)

def agregar_libro():
    for i, libro in enumerate(libros, 1):
        print(f"{i}.  {libro}")
    indice = int(input("Ingrese el numero de libro... ")) #no validado
    usuario_encontrado.add_libro(libros[indice-1]) 
    print("Libro agregado con exito... ")

def eliminar_libro():
    for i, libro in enumerate(libros, 1):
        print(f"{i}.  {libro}")
    indice = int(input("Ingrese el numero de libro... ")) #no validado
    usuario_encontrado.remove_libro(libros[indice-1]) 
    print("Libro eliminado con exito... ")

while True:

    print("Loggin... ")
    user_name = input("Ingrese su nombre de usuario...  ")
    user_pass = input("Ingrese su password... ")
    usuario_encontrado = loggin(user_name, user_pass)

    while not usuario_encontrado:
        print("Credenciales incorrectas.... ")
        user_name = input("Ingrese su nombre de usuario...  ")
        user_pass = input("Ingrese su password... ")
        usuario_encontrado = loggin(user_name, user_pass)

    while True:
        if(usuario_encontrado.administrator):
            print(menu_admin())
            while True:
                opt = input("Ingrese una opción... ")
                if (opt == '1' or opt == '2' or opt == '3' or opt == '7' ):
                    break
        else:
            while True:
                print(menu_usuario())
                opt = input("Ingrese una opción... ")
                if (opt == '4' or opt == '5' or opt == '6' or opt == '7'):
                    break

        if opt == '1':
            nuevo_usuario()
        if opt == '2':
            buscar_usuario()
        if opt == '3':
            buscar_libro()
        if opt == '4':
            for libro in usuario_encontrado.get_libros():
                print(libro)
        if opt == '5':
            agregar_libro()
        if opt == '6':
            eliminar_libro()
        if opt == '7':
            break
