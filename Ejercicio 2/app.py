from usuario import Usuario
from datetime import date

user = Usuario('jPerez', 'Juan', 'Perez', 'asd123', date(1994,4,9), '37569874', 'juanperez@gmail.com')

print(f"Bienvenido {user.apellido}, {user.nombre}")
print(f"Tu nombre de usuario es: {user.user_name}. Usted es usuario desde {user.fecha_alta}")
print(f"Su edad es: {user.edad}")

# TESTS 
assert user.validar_credenciales('jPerez', 'sda') == False
assert user.validar_credenciales('jPez', 'asd123') == False
assert user.validar_credenciales('jPerez', 'asd123') == True

try:
    user = Usuario()
    assert False, "No se puede instanciar un usuario sin nombre, apellido, username y password"
except TypeError:
    assert True