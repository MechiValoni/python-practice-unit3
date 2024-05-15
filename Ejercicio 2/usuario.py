'''
Tener en cuenta que este modelo no representa una implementación real en un sistema
La password nunca se almacena cómo texto plano si encriptar

1. ¿El atributo estado tiene un nombre representativo?
Proponer soluciones y mejoras.
2. ¿EL password debería tener un getter? Implementar sólo un setter sin getter que respete el modo de acceso con .
'''

from datetime import date
from persona import Persona

class Usuario(Persona):

    __users_names:set = set()

    def __init__(self, user_name:str, nombre:str, apellido:str, password:str, fecha_nacimiento:date, nro_documento:str, email:str) -> None:
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento)
        self.__user_name:str = Usuario.__validar_user_name(user_name)
        self.__password:str = password
        self.__estado:bool = True
        self.__fecha_alta:date = date.today()
        self.__fecha_baja:date = None
        self.__email:str = email

    @property
    def user_name(self) -> str:
        return self.__user_name
    
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
    
    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha:date) -> None:
        self.__fecha_baja = nueva_fecha

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, nuevo_email:str) -> None:
        self.__email = nuevo_email

    def baja_usuario(self) -> None:
        self.estado = False
        self.fecha_baja = date.today()

    def validar_credenciales(self, usuario:str, password:str) -> bool:
        return usuario == self.user_name and password == self.password
    
    @classmethod
    def __validar_user_name(cls, user_name:str) -> str:
        if user_name in cls.__users_names:
            raise Exception("El nombre de usuario ya está utilizado")
        
        cls.__users_names.add(user_name)
        return user_name
