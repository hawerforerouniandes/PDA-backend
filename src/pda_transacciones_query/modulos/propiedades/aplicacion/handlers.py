from pda_transacciones_query.seedwork.aplicacion.handlers import Handler
from pda_transacciones_query.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):
    
    @staticmethod
    def handle_asignar_transaccion(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'transaccionespda')

    @staticmethod
    def handle_transaccion_asignada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'transaccionespda')