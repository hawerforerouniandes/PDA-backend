from datetime import datetime

import pulsar
from pulsar.schema import AvroSchema

from pda_transacciones_command.modulos.propiedades.infraestructura.schema.v1.comandos import AsignarTransaccionPayload, \
    ComandoAsignarTransaccion
from pda_transacciones_command.modulos.propiedades.infraestructura.schema.v1.eventos import TransaccionAsignadaPayload, \
    EventoTransaccionAsignada
from pda_transacciones_command.seedwork.infraestructura import utils
import requests
from fastavro.schema import parse_schema
import json

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


        json_schema = requests.get(f'http://{HOSTNAME}:8080/admin/v2/schemas/public/default/transaccionespda/schema').json()
        avro_schema_json = json_schema['data']  # Extract the actual schema definition
        parsed_schema = parse_schema(json.loads(avro_schema_json))
        avro_schema = AvroSchema(None, schema_definition=parse_schema(parsed_schema))
     

        payload = TransaccionAsignadaPayload(
            id_propiedad=str(evento.id_propiedad),
            nombre_tomador=str(evento.nombre_tomador),
            nombre_propietario=str(evento.nombre_propietario)
        )
        evento_integracion = EventoTransaccionAsignada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionAsignada))

    def publicar_comando(self, comando, topico):

        json_schema = requests.get(f'http://{utils.broker_host()}:8080/admin/v2/schemas/public/default/transaccionespda/schema').json()
        avro_schema_json = json_schema['data']  # Extract the actual schema definition
        parsed_schema = parse_schema(json.loads(avro_schema_json))
        avro_schema = AvroSchema(None, schema_definition=parse_schema(parsed_schema))

        evento = {
            'id_propiedad':str(comando.id_propiedad),
            'nombre_tomador':str(comando.nombre_tomador),
            'nombre_propietario':str(comando.nombre_propietario)
        }

        print("Payload Asignar Transaccion: ", evento)
        self._publicar_mensaje(evento, topico, avro_schema)