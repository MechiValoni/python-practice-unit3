from abc import ABC, abstractmethod
from datetime import date

class Persona():

    @abstractmethod
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:date, nro_documento:str) -> None:
        self._nombre:str = nombre
        self._apellido:str = apellido
        self._nro_documento:str = nro_documento
        self._fecha_nacimento:date = fecha_nacimiento

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> None:
        self._nombre = nuevo_nombre 
    
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido:str) -> None:
        self._apellido = nuevo_apellido
    
    @property
    def nro_documento(self) -> str:
        return self._nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento:str) -> None:
        self._nro_documento = nuevo_nro_documento

    @property
    def fecha_nacimento(self) -> date:
        return self._fecha_nacimento
    
    @fecha_nacimento.setter
    def fecha_nacimento(self, nueva_fecha:date) -> None:
        self._fecha_nacimento = nueva_fecha

    @property
    def edad(self) -> int:
        today = date.today()
        born = self.fecha_nacimento
        age = today.year - born.year - int((today.month, today.day) < (born.month, born.day))
        return age