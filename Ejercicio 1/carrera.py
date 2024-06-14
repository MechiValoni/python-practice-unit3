from datetime import date
from titulo import Titulo
from typing import List

class Carrera():

    def __init__(self, nombre: str, comienzo: date) -> None:
        self.__nombre: str = nombre
        self.__comienzo: date = comienzo
        self.__titulos_grado_requerido: List[Titulo] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def comienzo(self) -> str:
        return f"{self.__comienzo.month}/{self.__comienzo.year}"
    
    @comienzo.setter
    def comienzo(self, nueva_fecha: date) -> None:
        self.__comienzo = nueva_fecha

    @property
    def titulos_grado_requerido(self) -> List[Titulo]:
        return self.__titulos_grado_requerido

    @property
    def cantidad_titulos_requeridos(self) -> int:
        return len(self.titulos_grado_requerido)

    def add_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.append(titulo)

    def remove_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.remove(titulo)

    def __str__(self) -> str:
        return f"{self.nombre} Comienzo: {self.comienzo} TR: [ {self.cantidad_titulos_requeridos} ]"

    