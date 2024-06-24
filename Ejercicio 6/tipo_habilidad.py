class TipoHabilidad():

    def __init__ (self, nombre: str) -> None:
        self.__nombre:str = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    def __str__(self) -> str:
        return f"Rama Arbol Habilidad: {self.nombre}"