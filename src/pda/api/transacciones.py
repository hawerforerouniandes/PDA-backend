import pulsar, _pulsar
from pulsar.schema import *
import os
import requests
import json



from pulsar.schema import *
from fastavro.schema import parse_schema

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")


json_schema = json_registry = requests.get(f'http://{HOSTNAME}:8080/admin/v2/schemas/public/default/transaccionespda/schema').json()
avro_schema_json = json_schema['data']  # Extract the actual schema definition
parsed_schema = parse_schema(json.loads(avro_schema_json))
avro_schema = AvroSchema(None, schema_definition=parse_schema(parsed_schema));
client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')

consumer = client.subscribe('transaccionespda', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedades-transacciones', schema=avro_schema)



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
producer.send(data)

# Close the producer when done
producer.close()

# Continuous loop to receive messages
try:
    while True:
        msg = consumer.receive()
        try:
            # Process the message
            print(f'Evento recibido: {msg.value()}')
            # Acknowledge successful processing of the message
            consumer.acknowledge(msg)
        except Exception as e:
            print("Failed to process message:", str(e))
            # Negative acknowledgement in case of failure
            consumer.negative_acknowledge(msg)
except KeyboardInterrupt:
    print("Stopped by user")

# Close the consumer and client before exiting
consumer.close()
client.close()