
class Titulo():

    def __init__ (self, nombre: str, universidad: str = "Extranjera") -> None:
        self.__nombre: str = nombre
        self.__universidad: str = universidad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def universidad(self) -> str:
        return self.__universidad

    @universidad.setter
    def universidad(self, nueva_universidad: str) -> None:
        self.__universidad = nueva_universidad

    def __str__(self) -> str:
        return f"Titulo: {self.nombre} expedido por {self.universidad}"