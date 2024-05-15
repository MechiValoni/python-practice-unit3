from usuario import Usuario
from datetime import date

user = Usuario('jPerez', 'Juan', 'Perez', 'asd123')

print(f"Bienvenido {user.apellido}, {user.nombre}")
print(f"Tu nombre de usuario es: {user.user_name}. Usted es usuario desde {user.fecha_alta}")

# TESTS 
user = Usuario('jPerez', 'Juan', 'Perez', 'asd123')
assert user.validar_credenciales('jPerez', 'sda') == False
assert user.validar_credenciales('jPez', 'asd123') == False
assert user.validar_credenciales('jPerez', 'asd123') == True

try:
    user = Usuario()
    assert False, "No se puede instanciar un usuario sin nombre, apellido, username y password"
except TypeError:
    assert True

try:
    user = Usuario('jPerez', 'Juan', 'Perez', 'asd123')
    user.user_name = 'JPEREZ'
    assert False, "No se puede modificar el nombre de usuario"
except AttributeError:
    assert True

user = Usuario('jPerez', 'Juan', 'Perez', 'asd123')
user.baja_usuario()
assert user.fecha_baja == date.today()
assert user.estado == False