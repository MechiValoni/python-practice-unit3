'''
Tener en cuenta que este modelo no representa una implementación real en un sistema
La password nunca se almacena cómo texto plano si encriptar

1. ¿Tine sentido que la fecha_alta se pueda modificar?
2. ¿El atributo estado tiene un nombre representativo?
Proponer soluciones y mejoras.
3. ¿EL password debería tener un getter? Implementar sólo un setter sin getter que respete el modo de acceso con .
'''

from datetime import date

class Usuario():

    def __init__(self, user_name:str, nombre:str, apellido:str, password:str) -> None:
        self.__user_name:str = user_name
        self.__nombre:str = nombre
        self.__apellido:str = apellido
        self.__password:str = password
        self.__estado:bool = True
        self.__fecha_alta:date = date.today()
        self.__fecha_baja:date = None

    @property
    def user_name(self) -> str:
        return self.__user_name
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> None:
        self.__nombre = nuevo_nombre 
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido:str) -> None:
        self.__apellido = nuevo_apellido
    
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, nueva_password:str) -> None:
        self.__password = nueva_password
    
    @property
    def estado(self) -> bool:
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado:bool) -> None:
        self.__estado = nuevo_estado
    
    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @fecha_alta.setter
    def fecha_alta(self, nueva_fecha:date) -> None:
        self.__fecha_alta = nueva_fecha
    
    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha:date) -> None:
        self.__fecha_baja = nueva_fecha

    def baja_usuario(self) -> None:
        self.estado = False
        self.fecha_baja = date.today()

    def validar_credenciales(self, usuario:str, password:str) -> bool:
        return usuario == self.user_name and password == self.password
