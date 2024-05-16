from abc import ABC, abstractmethod
from datetime import date
from tipo_documento import TipoDocumento

class Persona(ABC):

    #decoro el constructor con abstactmethod para impedir que se cree un obj de esta clase
    @abstractmethod
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:date, nro_documento:int, tipo_documento:TipoDocumento) -> None:
        self._nombre = nombre #atributo protejido
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._nro_documento = nro_documento
        #este metodo el constructor se ejecuta una unica vez, durante toda la existencia del obj.
        self._tipo_documento = tipo_documento #atributo de tipo TipoDocumento

    def get_edad(self) -> int:
        return date.today().year - self.get_fecha_nacimiento().year

    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, new_nombre:str):
        self._nombre = new_nombre

    def get_apellido(self) -> date: #recupera el valor almacenado
        return self._apellido
    
    def set_apellido(self, new_apellido:str): #modifica el valor almacenado
        self._apellido = new_apellido

    def get_fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento
    
    def set_fecha_nacimiento(self, new_fecha_nacimiento:date):
        self._fecha_nacimiento = new_fecha_nacimiento
    
    def get_nro_documento(self) -> int:
        return self._nro_documento
    
    def set_nro_documento(self, new_nro_documento:int):
        self._nro_documento = new_nro_documento

    def get_tipo_documento(self) -> TipoDocumento:
        return self._tipo_documento
    
    def set_tipo_documento(self, new_tipo_documento:TipoDocumento):
        self._tipo_documento = new_tipo_documento