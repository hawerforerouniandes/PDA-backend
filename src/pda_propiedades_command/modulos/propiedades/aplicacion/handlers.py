from pda_propiedades_command.seedwork.aplicacion.handlers import Handler
from pda_propiedades_command.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):
    
    @staticmethod
    def handle_asignar_transaccion(evento):
        despachador = Despachador()
        despachador.publicar_comando(evento, 'transaccionespda')

    @staticmethod
    def handle_transaccion_asignada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'transaccionespda')

    @staticmethod
    def handle_publicar_sagalog(evento):
        despachador = Despachador()
        despachador.publicar_evento_sagalog(evento, 'saga-log')