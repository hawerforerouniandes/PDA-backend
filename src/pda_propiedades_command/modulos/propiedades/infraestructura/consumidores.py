import pulsar,_pulsar  
from pulsar.schema import *
from fastavro.schema import parse_schema
import uuid
import time
import logging
import traceback
import os
import requests
import json

from pda_propiedades_command.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from pda_propiedades_command.modulos.transacciones.aplicacion.dto import TransaccionDTO


def suscribirse_transacciones_update():
    cliente = None
    try:

        HOSTNAME = os.getenv('PULSAR_ADDRESS', default="10.128.0.5")

        json_schema = requests.get(f'http://{HOSTNAME}:8080/admin/v2/schemas/public/default/propiedades/schema').json()
        avro_schema_json = json_schema['data']  # Extract the actual schema definition
        parsed_schema = parse_schema(json.loads(avro_schema_json))
        avro_schema = AvroSchema(None, schema_definition=parse_schema(parsed_schema))
        client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')

        logging.info("**************consumer-propiedades")
        consumer = client.subscribe('propiedades', consumer_type=pulsar.ConsumerType.Shared, subscription_name='propiedades-transacciones-update', schema=avro_schema)

        while True:
            mensaje = consumer.receive()
            print(f'Evento recibido desde propiedades: {mensaje.value()}')
            try:
                transaccion_dto = TransaccionDTO(id_transaccion=mensaje.value().get('id_transaccion'), id_propiedad=mensaje.value().get('id_propiedad'), nombre_propietario="", nombre_tomador="")
                sp = ServicioPropiedad()
                sp.actualizar_propiedad_con_transaccion(transaccion_dto)
                consumer.acknowledge(mensaje)
            except Exception as e:
                logging.error('ERROR: Error al consumir mensaje')

    except:
        cliente.close()
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()