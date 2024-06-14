import code_generator

class Usuario():

    __ids = set()

    def __init__(self, nombre:str, apellido:str, email:str, password:str) -> None:
        self.__id: int = Usuario.__obtener_id()
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__email: str = email
        self.__password: str = password

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido) -> None:
        self.__apellido = nuevo_apellido

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, nuevo_email) -> None:
        self.__email = nuevo_email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, nuevo_password) -> None:
        self.__password = nuevo_password

    def validar_credenciales(self, email:str, password:str) -> bool:
        return self.email == email and self.password == password
    
    @classmethod
    def __obtener_id(cls) -> int:
        cod = code_generator.generated_code()
        while (cod in cls.__ids):
            cod = code_generator.generated_code() 
        cls.__ids.add(cod) 
        return cod

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

