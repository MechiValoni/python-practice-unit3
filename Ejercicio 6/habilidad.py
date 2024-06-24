from tipo_habilidad import TipoHabilidad
from typing import Self

class Habilidad():

    def __init__(self, nombre: str, tipo_habilidad: TipoHabilidad, puntos_maximo: int, habilidad_desbloqueada_requerida:Self = None) -> None:
        self.__nombre:str = nombre
        self.__tipo_habilidad:TipoHabilidad = tipo_habilidad
        self.__habilidad_desbloqueada_requerida:Habilidad = habilidad_desbloqueada_requerida
        self.__puntos_maximo:int = puntos_maximo
        self.__cantidad_puntos_otorgados:int = int(0)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self):
        return self.__nombre

    @property
    def tipo_habilidad(self) -> str:
        return self.__tipo_habilidad

    @property
    def habilidad_desbloqueada_requerida(self) -> Self:
        return self.__habilidad_desbloqueada_requerida

    @property
    def puntos_maximo(self) -> int:
        return self.__puntos_maximo

    @property
    def maximo_alcanzado(self) -> bool:
        return self.cantidad_puntos_otorgados >= self.puntos_maximo

    @property
    def cantidad_puntos_otorgados(self) -> int:
        return self.__cantidad_puntos_otorgados

    def mejorar_habilidad(self) -> None:
        self.__cantidad_puntos_otorgados += 1

    def __str__(self):
        return f''' {self.nombre} [{self.tipo_habilidad.nombre}]
        P:({self.cantidad_puntos_otorgados}){' Máximo alcanzado: SI' if self.maximo_alcanzado else ''}{' Habilidad Requerida: ' + self.habilidad_desbloqueada_requerida.nombre if self.habilidad_desbloqueada_requerida else ''}'''