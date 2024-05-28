from datetime import date
from code_generator import *

class Libro():

    #aca van los atributos de clase
    __list_isbn = [] #lista vacia de isbn, compartida por todas las instancias de la clase libro

    def __init__(self, nombre:str, fecha_lanzamiento: date, autor:str = "Unknow") -> None:
        #aca van los atributos de instancia
        self.cantidad_paginas = 100
        self.__nombre = nombre #atributo privado
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__autor = autor
        self.__isbn = Libro.generar_ISBN()

    def get_isbn(self) -> str:
        return self.__isbn
    
    def set_isbn(self, new_isbn:str): #setter condicionado
        if (new_isbn in Libro.__list_isbn):
            raise Exception("ERROR, EL ISBN NO ES UNICO")
        Libro.__list_isbn.append(new_isbn)
        self.__isbn = new_isbn
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, new_nombre:str):
        self.__nombre = new_nombre
    
    @property #getter
    def fecha_lanzamiento(self) -> date:
        return self.__fecha_lanzamiento

    @fecha_lanzamiento.setter #setter
    def fecha_lanzamiento(self, new_fecha_lanzamiento:date):
        self.__fecha_lanzamiento = new_fecha_lanzamiento

    def get_autor(self) -> date: #recupera el valor almacenado
        return self.__autor
    
    def set_autor(self, new_autor:str): #modifica el valor almacenado
        self.__autor = new_autor

    @classmethod #metodo de clase
    def generar_ISBN(cls) -> str:   
        cod = generated_code()
        while (cod in Libro.__list_isbn):
            cod = generated_code() #pido en bucle que se genere un codigo hasta que el mismo sea unico, NO ESTE EN LA LISTA __list_isbn
        Libro.__list_isbn.append(cod) #agrego el codigo nuevo, para dejarlo guardado en la lista
        return cod
    
    def __str__(self) -> str:
        return f"{self.get_autor()}: {self.get_nombre()} [{self.get_isbn()}]"