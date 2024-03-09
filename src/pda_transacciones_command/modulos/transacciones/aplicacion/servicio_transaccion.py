
from pda_transacciones_command.modulos.transacciones.aplicacion.dto import TransaccionDTO
from pda_transacciones_command.modulos.transacciones.aplicacion.handlers import HandlerPropiedadIntegracion
from pda_transacciones_command.modulos.transacciones.infraestructura.adaptador_firestore import TransaccionRepository, FirestoreTransaccionRepository
from pda_transacciones_command.modulos.transacciones.infraestructura.adaptador_pulsar import AdaptadorPulsar
from pda_transacciones_command.modulos.transacciones.dominio.entidades import Transaccion

class ServicioTransaccion:
    def __init__(self):

        self.firebase_adapter: TransaccionRepository  = FirestoreTransaccionRepository()
        self.pulsa_adapter : AdaptadorPulsar = AdaptadorPulsar()

    def procesar_transaccion_recibida(self, data: Transaccion):
        # Lógica para procesar una transacción recibida
        HandlerPropiedadIntegracion.handle_publicar_sagalog(data, 'Servicio Transaccion',
                                                            'transacciones-command', 'Entro a guardar Transaccion BD')
        transaccion = self.firebase_adapter.add(data)
        HandlerPropiedadIntegracion.handle_publicar_sagalog(data, 'Servicio Transaccion',
                                                            'transacciones-command', 'Finalizo guardar Transaccion BD')
        HandlerPropiedadIntegracion.handle_publicar_sagalog(data, 'Servicio Transaccion',
                                                            'transacciones-command', 'Entro a publicar Evento')
        self.pulsa_adapter.emitEvent(
            {
                "id_transaccion": transaccion["id_transaccion"],
                "id_propiedad": transaccion["id_propiedad"]
            }
            )
        HandlerPropiedadIntegracion.handle_publicar_sagalog(data, 'Servicio Transaccion',
                                                            'transacciones-command', 'Finalizo publicar Evento')
        pass

    def obtener_transaccion_por_id(self, id_transaccion) -> TransaccionDTO:
        HandlerPropiedadIntegracion.handle_publicar_sagalog(id_transaccion, 'Servicio Transaccion',
                                                            'transacciones-command', 'Entro a obtener transaccion por id')
        return self.firebase_adapter.get(id_transaccion)