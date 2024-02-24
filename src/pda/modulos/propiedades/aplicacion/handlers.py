from pda.seedwork.aplicacion.handlers import Handler
from pda.modulos.vuelos.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):
    
    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')