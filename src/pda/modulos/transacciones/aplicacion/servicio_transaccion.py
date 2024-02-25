
from pda.modulos.transacciones.infraestructura.adaptador_firestore import TransaccionRepository, FirestoreTransaccionRepository
from pda.modulos.transacciones.infraestructura.adaptador_pulsar import AdaptadorPulsar
from pda.modulos.transacciones.dominio.entidades import Transaccion

class ServicioTransaccion:
    def __init__(self):

        self.firebase_adapter: TransaccionRepository  = FirestoreTransaccionRepository()
        self.pulsa_adapter : AdaptadorPulsar = AdaptadorPulsar()

    def procesar_transaccion_recibida(self, data: Transaccion):
        # Lógica para procesar una transacción recibida

        transaccion = self.firebase_adapter.add(data)
        self.pulsa_adapter.emitEvent(
            {
                "id_transaccion": transaccion["id_transaccion"],
                "id_propiedad": transaccion["id_propiedad"]
            }
            )
        pass