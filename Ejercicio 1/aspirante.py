from titulo import Titulo
from typing import List

class Aspirante():

    def __init__ (self, nombre: str, apellido: str, email: str, num_telefono: str) -> None:
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__email: str = email
        self.__num_telefono: str = num_telefono
        self.__titulos: List[Titulo] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido: str) -> None:
        self.__apellido = nuevo_apellido

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, nuevo_email: str) -> None:
        self.__email = nuevo_email

    @property
    def num_telefono(self) -> str:
        return self.__num_telefono

    @num_telefono.setter
    def num_telefono(self, nuevo_num: str) -> None:
        self.__num_telefono = nuevo_num

    @property
    def titulos(self) -> List[Titulo]:
        return self.__titulos

    def add_titulo(self, titulo: Titulo) -> None:
        self.__titulos.append(titulo)

    def remove_titulo(self, titulo: Titulo) -> None:
        self.__titulos.remove(titulo)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} Contacto: {self.email} - {self.num_telefono}"