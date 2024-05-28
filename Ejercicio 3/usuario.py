from datetime import date
from persona import Persona
from datetime import date
from libro import Libro
from tipo_documento import TipoDocumento

class Usuario(Persona):

    __list_user_name = [] #atributo de clase

    def __init__(self, user_name:str, password:str, email:str, nombre: str, apellido: str, fecha_nacimiento: date, nro_documento: int, tipo_documento:TipoDocumento,administrator:bool = False) -> None:
        self.__user_name = Usuario.__validar_user_name(user_name)
        self.__password = password
        self.__estado = True #no recibivo el valor por parametro en el constructor, porque lo seteo derecho.
        self.__administrator = administrator
        self.__email = email
        self.__fecha_alta = date.today() #genero la fecha del dia
        self.__fecha_baja = None #Nulo
        self.__libros = [] #lista vacia de libros del usuario, mapeo relación que termina en *
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento) #llamo al constructor de la clase padre, con sus respectivos argumentos
    
    @property
    def administrator(self) -> bool:
        return self.__administrator

    def get_user_name(self) -> str:
        return self.__user_name
    
    def get_fecha_alta(self) -> date:
        return self.__fecha_alta
    
    #faltan los getter y setters restantes...

    def get_libros(self) -> list: # getter de la lista
        return self.__libros

    #libro:Libro no es una llamada al constructor, es un typehint
    def add_libro(self, libro:Libro): #agrega un obj Libro a la lista __libros que surge de mi relacion con la clase Libro
        self.__libros.append(libro)

    def remove_libro(self, libro:Libro): #remueve el obj Libro de la lista
        self.__libros.remove(libro)

    def leyo_libro(self, isbn:str) -> bool:
        for libro in self.get_libros(): #recorro toda mi lista de libros
            if libro.get_isbn() == isbn: 
                return True #si el libro encontrado, retorno True
        return False #si no encuentra un libro con el mismo isbn (cod idenficador unico para un libro) en toda mi lista retorno False

    def baja_usuario(self):
        self.__estado = False
        self.__fecha_baja = date.today()

    #valida que el user_name y password pasado coincida con lo almacenado en los atributos del objeto
    def validar_credenciales(self, user_name:str, password:str) -> bool:
        return self.__user_name == user_name and self.__password == password

    @classmethod
    def __validar_user_name(cls, user_name:str) -> str:
        if (user_name in Usuario.__list_user_name):
            raise Exception("Error! User name ya utilizado.")
        Usuario.__list_user_name.append(user_name)
        return user_name
    
    def __str__(self) -> str:
        return f"{self.get_apellido()}, {self.get_nombre()}"