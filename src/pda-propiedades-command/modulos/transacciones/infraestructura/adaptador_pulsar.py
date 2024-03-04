import pulsar
from pulsar.schema import *
import os
from fastavro.schema import parse_schema
import json
import requests

class AdaptadorPulsar :
    def __init__(self):
        self.host = os.getenv('PULSAR_ADDRESS', default="10.128.0.5")
        self.client = pulsar.Client(f'pulsar://{self.host}:6650')

    def emitEvent(self, message):
        # Create a producer
        producer = self.client.create_producer(
            topic='propiedades',
            schema=self.loadSchema()
        )

        # Example message

        # Send the message
        producer.send(message)

        # Close the producer when done
        producer.close()


    def loadSchema(self):
        json_schema = requests.get(f'http://{self.host}:8080/admin/v2/schemas/public/default/propiedades/schema').json()
        avro_schema_json = json_schema['data']  # Extract the actual schema definition
        parsed_schema = parse_schema(json.loads(avro_schema_json))
        return AvroSchema(None, schema_definition=parse_schema(parsed_schema))
        