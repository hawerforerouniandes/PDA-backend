from datetime import datetime

import pulsar
from pulsar.schema import AvroSchema

from pda.modulos.propiedades.infraestructura.schema.v1.comandos import AsignarTransaccionPayload, \
    ComandoAsignarTransaccion
from pda.modulos.propiedades.infraestructura.schema.v1.eventos import TransaccionAsignadaPayload, \
    EventoTransaccionAsignada
from pda.seedwork.infraestructura import utils

epoch = datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = TransaccionAsignadaPayload(
            id_propiedad=str(evento.id_propiedad),
            nombre_tomador=str(evento.nombre_tomador),
            nombre_propietario=str(evento.nombre_propietario)
        )
        evento_integracion = EventoTransaccionAsignada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionAsignada))

    def publicar_comando(self, comando, topico):
        payload = AsignarTransaccionPayload(
            id_propiedad=str(comando.id_propiedad),
            nombre_tomador=str(comando.nombre_tomador),
            nombre_propietario=str(comando.nombre_propietario)
        )
        print("Payload Asignar Transaccion: ", payload)
        comando_integracion = ComandoAsignarTransaccion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoAsignarTransaccion))