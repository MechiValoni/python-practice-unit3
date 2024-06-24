from tipo_habilidad import TipoHabilidad
from habilidad import Habilidad
from personaje import Personaje
from typing import List

'''
    Combate (Tipo Habilidad):
        Ataque rapido (Habilidad)
        Defensa (Habilidad)
            Contraataque (Habilidad)
    Alquimia (Tipo Habilidad):
        Tolerancia Superior (Habilidad)
            Rendimiento (Habilidad)
'''

#inicializo lista vacía
habilidades:List[Habilidad] = []

#genero tipos de habilidades
tipo_habilidad_combate:TipoHabilidad = TipoHabilidad('Combate')
tipo_habilidad_alquimia:TipoHabilidad = TipoHabilidad('Alquimia')

#genero las habilidades
habilidad_ataque:Habilidad = Habilidad('Ataque Rapido', tipo_habilidad_combate, 2) 
habilidad_defensa:Habilidad = Habilidad('Defensa', tipo_habilidad_combate, 1)
habilidad_contrataque:Habilidad = Habilidad('Contraataque', tipo_habilidad_combate, 2, habilidad_desbloqueada_requerida=habilidad_defensa)
habilidad_tolerancia:Habilidad = Habilidad('Tolerancia Superior', tipo_habilidad_alquimia, 5)
habilidad_rendimiento:Habilidad = Habilidad('Rendimiento', tipo_habilidad_alquimia, 2, habilidad_desbloqueada_requerida=habilidad_tolerancia)

#agrego las habilidades a la lista de habilidades disponibles para el personaje
habilidades.append(habilidad_ataque)
habilidades.append(habilidad_defensa)
habilidades.append(habilidad_contrataque)
habilidades.append(habilidad_tolerancia)
habilidades.append(habilidad_rendimiento)

#creo un personaje
habilidades[0].mejorar_habilidad()
personaje = Personaje('Geralt', habilidades[0])
personaje.subir_nivel()
personaje.mejorar_habilidad(habilidades[1])
personaje.subir_nivel()
personaje.subir_nivel()
personaje.mejorar_habilidad(habilidades[2])
personaje.subir_nivel()
personaje.mejorar_habilidad(habilidades[3])
personaje.subir_nivel()
personaje.subir_nivel()
personaje.mejorar_habilidad(habilidades[0])