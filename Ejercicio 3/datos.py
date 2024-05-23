#DB
#aca van todos los objetos "Almacenados"
from tipo_documento import TipoDocumento
from libro import Libro
from datetime import date
from usuario import Usuario

tipos_documento = [TipoDocumento('dni'), 
                   TipoDocumento('lc'),
                   TipoDocumento('pasaporte')]


libros = [Libro('El principito', date(1960,5,22), "Jorge Landeta"),
          Libro('La Naranja Mecanica', date(1980,12,1)), 
          Libro(nombre='Don quijote', fecha_lanzamiento=date(1920,3,30), autor='Servantes')]


tipo_dni = tipos_documento[0]
usuarios = [Usuario('mvaloni','ads123','mechi@gmail.com','Mercedes', 'Valoni', date(1998, 6, 2), 33333333, tipo_dni, True),
            Usuario('cristopher','banana','c@gmail.com','Cristopher', 'Ninotti', date(1989, 2, 2), 33333333, tipo_dni)]