from aspirante import Aspirante
from carrera import Carrera
from titulo import Titulo
from inscripcion import Inscripcion
from datetime import date

#inicializo lista vacía
inscripciones = []

aspirante = Aspirante("Juan", "Perez", "perezjuan@gmail.com", "+5493416214584")

titulos = [
    Titulo("Ingeniero Mecánico","Universidad Tecnologica Nacional"),
    Titulo("Contador Público Nacional","Universidad Nacional de Rosario"),
    Titulo("Ingeniería Civil Mecanica")
]

carreras = [
    Carrera("Maestria en Ciencia de los Materiales",date(2024,4,2)),
    Carrera("Doctorado en Finanzas",date(2024,3,28))
]

#agrego titulos al aspirante
aspirante.add_titulo(titulos[0])

#agrego titulos de grado requeridos a cada carrera de postgrado
carreras[0].add_titulo_requerido(titulos[0]) 
carreras[0].add_titulo_requerido(titulos[2])
carreras[1].add_titulo_requerido(titulos[1])

#genero una inscripcion
x = Inscripcion(aspirante, carreras[0])
inscripciones.append(x)