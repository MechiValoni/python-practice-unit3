from datetime import *
from precio import Precio

class Estadia():

    __patentes = set()

    #Se deja con un defalt la hora entrada sólo para hacer más sencillas las pruebas
    def __init__(self, patente:str, hora=datetime.now().time()) -> None:
        self.__patente = Estadia.__validar_patente(patente)
        self.__fecha = date.today()
        self.__hora_entrada = hora#datetime.now().time()
        self.__hora_salida = None
        self.__estado = 'Activo'
        self.__pagado = False

    @property
    def patente(self) -> str:
        return self.__patente

    @patente.setter
    def patente(self, new_patente):
        self.__patente = new_patente

    @property
    def estado(self) -> str:
        return self.__estado

    @estado.setter
    def estado(self, new_estado):
        self.__estado = new_estado

    @property
    def fecha(self) -> date:
        return self.__fecha

    @fecha.setter
    def fecha(self, new_fecha):
        self.__fecha = new_fecha

    @property
    def hora_entrada(self) -> time:
        return self.__hora_entrada

    @hora_entrada.setter
    def hora_entrada(self, new_hora_entrada):
        self.__hora_entrada = new_hora_entrada

    @property
    def hora_salida(self) -> time:
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, new_hora_salida):
        self.__hora_salida = new_hora_salida

    @property
    def pagado(self) -> bool:
        return self.__pagado

    @pagado.setter
    def pagado(self, new_pagado):
        self.__pagado = new_pagado

    @property
    def cant_horas(self) -> int:
        horas = self.hora_salida.hour - self.hora_entrada.hour
        minutos = self.hora_salida.minute - self.hora_entrada.minute
        if minutos > 30:
            horas = horas + 1
        return horas

    @classmethod
    def __validar_patente(cls, patente:str) -> str:
        if patente in cls.__patentes:
            raise Exception("Patente duplicada...")
        cls.__patentes.add(patente)
        return patente

    def registrar_salida(self) -> float:
        self.pagado = True
        self.hora_salida = datetime.now().time()
        return Precio.calcular_importe(self.cant_horas)

    def __str__(self) -> str:
        return '''Fecha: {fecha}
        Patete: {patente}
        Hora Entrada: {horae}
        Hora Salida: {horas}
        Pagado: {pagado}'''.format(fecha = self.fecha, 
                                patente = self.patente,
                                horae = f"{self.hora_entrada.hour}:{self.hora_entrada.minute}",
                                horas = f"{self.hora_salida.hour}:{self.hora_salida.minute}" if self.hora_salida else "--:--",
                                pagado = self.pagado)
        