import threading
import pulsar
from pulsar.schema import *
import os
import requests
import json

from pda_transacciones_command.modulos.transacciones.aplicacion.handlers import HandlerPropiedadIntegracion
from pda_transacciones_command.modulos.transacciones.aplicacion.mapeadores import MapeadorTransaccionDTOJson, MapeadorTransaccion
from pda_transacciones_command.modulos.transacciones.aplicacion.servicio_transaccion import ServicioTransaccion
from fastavro.schema import parse_schema

def start_pulsar_consumer():
    HOSTNAME = os.getenv('PULSAR_ADDRESS', default="35.222.56.106")

    json_schema = requests.get(f'http://{HOSTNAME}:8080/admin/v2/schemas/public/35.222.56.106/schema').json()
    avro_schema_json = json_schema['data']  # Extract the actual schema definition
    parsed_schema = parse_schema(json.loads(avro_schema_json))
    avro_schema = AvroSchema(None, schema_definition=parse_schema(parsed_schema))
    client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')



    # Create a producer
    producer = client.create_producer(
        topic='transaccionespda',
        schema=avro_schema
    )

    # Example message
    data = {
        "id_propiedad": "some_id",
        "nombre_tomador": "some_name",
        "nombre_propietario": "another_name"
    }

    # Send the message
    #producer.send(data)

    # Close the producer when done
    #producer.close()

    consumer = client.subscribe('transaccionespda', consumer_type=pulsar.ConsumerType.Shared, subscription_name='propiedades-transacciones', schema=avro_schema)

    try:
        while True:
            msg = consumer.receive()
            try:
                # Process the message
                print(f'Evento recibido desde transacciones: {msg.value()}')
                HandlerPropiedadIntegracion.handle_publicar_sagalog(msg.value(), 'Api Transacciones',
                                                                    'transacciones-command', 'Evento recibido')
                mapeadorTransaccionDTOJson = MapeadorTransaccionDTOJson()
                mapeadorTransaccion = MapeadorTransaccion()

                servicioTransaccion = ServicioTransaccion()

                transaccion = mapeadorTransaccion.dto_a_entidad(mapeadorTransaccionDTOJson.externo_a_dto(msg.value()))
                servicioTransaccion.procesar_transaccion_recibida(transaccion)

                print("finalizo el proceso")
                # Acknowledge successful processing of the message
                consumer.acknowledge(msg)
            except Exception as e:
                print("Failed to process message:", str(e))
                # Negative acknowledgement in case of failure
                consumer.negative_acknowledge(msg)
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        # Close the consumer and client before exiting
        consumer.close()
        client.close()

# Create a thread for running the Pulsar consumer
pulsar_thread = threading.Thread(target=start_pulsar_consumer)
pulsar_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
pulsar_thread.start()

# Your web server startup code here
# Start your web server without blocking
