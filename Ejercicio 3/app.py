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
            nuevo_usuario = Usuario(user, passw, '', nombre, apellido, date(anio, mes, dia), 5, tipos_documento[indice-1])
            usuarios.append(nuevo_usuario)
            
        if opt == '2':
            user = input("Ingrese un nombre de usuario que desea buscar: ")
            for usuario in usuarios: 
                if usuario.get_user_name() == user:
                    print(usuario)
                    break
        if opt == '3':
            print(f"3")
        if opt == '4':
            for i, libro in enumerate(libros, 1):
                print(f"{i}.  {libro}")
        if opt == '5':
            print(f"5")
        if opt == '6':
            print(f"6")
        if opt == '7':
            break
