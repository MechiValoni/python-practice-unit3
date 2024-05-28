class Precio():

    __precio_hora = float(1500)

    @classmethod
    def calcular_importe(cls, cant_horas:int) -> float:
        return cant_horas * cls.__precio_hora