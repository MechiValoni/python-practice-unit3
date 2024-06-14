class Tag():

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    def __str__(self) -> str:
        return f"{self.nombre}"