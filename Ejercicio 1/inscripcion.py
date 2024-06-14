from aspirante import Aspirante
from carrera import Carrera
from datetime import date

class Inscripcion():

    __ant_num = int(0)

    def __init__(self, aspirante: Aspirante, carrera: Carrera) -> None:
        self.__aspirante: Aspirante = aspirante
        self.__carrera: Carrera = carrera
        self.__fecha_inscripcion: date = date.today()
        self.__inscripcion_activa: bool = True
        self.__nro: int = Inscripcion.__get_prox_num()

    @property
    def aspirante(self) -> Aspirante:
        return self.__aspirante
    
    @property
    def carrera(self) -> Carrera:
        return self.__carrera

    @property
    def fecha_inscripcion(self) -> date:
        return self.__fecha_inscripcion

    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa

    @inscripcion_activa.setter
    def inscripcion_activa(self, nuevo_estado:bool) -> None:
        self.__inscripcion_activa = nuevo_estado

    @property
    def nro(self) -> int:
        return self.__nro

    @classmethod
    def __get_prox_num(cls) -> int:
        cls.__ant_num += 1
        return cls.__ant_num

    def __str__(self) -> str:
        return f"Inscripción número {self.nro}, Aspirante: {self.aspirante.nombre} {self.aspirante.apellido}, Carrera: {self.carrera.nombre}"