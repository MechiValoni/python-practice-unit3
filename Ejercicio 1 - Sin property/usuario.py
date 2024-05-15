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

    def get_user_name(self) -> str:
        return self.__user_name
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre:str) -> None:
        self.__nombre = nuevo_nombre 
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, nuevo_apellido:str) -> None:
        self.__apellido = nuevo_apellido
    
    def get_password(self) -> str:
        return self.__password

    def set_password(self, nueva_password:str) -> None:
        self.__password = nueva_password
    
    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, nuevo_estado:bool) -> None:
        self.__estado = nuevo_estado
    
    def get_fecha_alta(self) -> date:
        return self.__fecha_alta
    
    def set_fecha_alta(self, nueva_fecha:date) -> None:
        self.__fecha_alta = nueva_fecha
    
    def get_fecha_baja(self) -> date:
        return self.__fecha_baja
    
    def set_fecha_baja(self, nueva_fecha:date) -> None:
        self.__fecha_baja = nueva_fecha

    def baja_usuario(self) -> None:
        self.estado = False
        self.fecha_baja = date.today()

    def validar_credenciales(self, usuario:str, password:str) -> bool:
        return usuario == self.user_name and password == self.password
