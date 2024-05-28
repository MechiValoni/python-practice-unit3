from estadia import Estadia
import datetime

estadias = [Estadia('EFF694', datetime.time(7, 00)),
            Estadia('ABC123', datetime.time(6, 50))
]

estadias[0].registrar_salida()
