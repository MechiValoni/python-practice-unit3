
class TipoDocumento():

    def __init__(self, tipo_documento:str) -> None:
        self.__tipo_documento = tipo_documento

    def get_tipo_documento(self) -> str:
        return self.__tipo_documento
    
    def __str__(self) -> str:
        return self.get_tipo_documento().upper()
    
    