from habilidad import Habilidad
from typing import List

class Personaje():

    __nombres = set()

    def __init__(self, nombre: str, habilidad_inicial: Habilidad) -> None:
        self.__nombre: str = Personaje.__validar_nombre(nombre)
        self.__arbol_habilidades: List[Habilidad] = [habilidad_inicial]
        self.__cantidad_puntos_nivel: int = int(1)

    @property
    def arbol_habilidades(self) -> List[Habilidad]:
        return self.__arbol_habilidades

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def cantidad_puntos_nivel(self) -> int:
        return self.__cantidad_puntos_nivel

    @property
    def cantidad_puntos_disponible(self) -> int:
        return self.cantidad_puntos_nivel - sum([h.cantidad_puntos_otorgados for h in self.arbol_habilidades])

    def mejorar_habilidad(self, habilidad: Habilidad) -> None:
        if self.cantidad_puntos_disponible > 0 and not habilidad.habilidad_desbloqueada_requerida or (habilidad.habilidad_desbloqueada_requerida in self.arbol_habilidades):
            habilidad.mejorar_habilidad()
            if not habilidad in self.arbol_habilidades:
                self.arbol_habilidades.append(habilidad)
        else:
            raise Exception("Error")

    @classmethod
    def __validar_nombre(cls, nombre: str) -> str:
        if nombre in cls.__nombres:
            raise Exception("Error")
        Personaje.__nombres.add(nombre)
        return nombre

    def subir_nivel(self) -> None:
        self.__cantidad_puntos_nivel += 1

    def __str__(self):
        return f'''Nombre: {self.nombre} - Nivel: {self.cantidad_puntos_nivel}
        Habilidades en el Arbol: {[h.nombre for h in self.arbol_habilidades if h.cantidad_puntos_otorgados > 0]}
        Puntos disponibles: {self.cantidad_puntos_disponible}'''