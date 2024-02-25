
from src.pda.modulos.transacciones.infraestructura.adaptador_firestore import TransaccionRepository, FirestoreTransaccionRepository
from src.pda.modulos.transacciones.dominio.entidades import Transaccion

class ServicioTransaccion:
    def __init__(self):

        self.firebase_adapter: TransaccionRepository  = FirestoreTransaccionRepository()

    def procesar_transaccion_recibida(self, data: Transaccion):
        # Lógica para procesar una transacción recibida

        print(data)
        self.firebase_adapter.add(data)
        pass