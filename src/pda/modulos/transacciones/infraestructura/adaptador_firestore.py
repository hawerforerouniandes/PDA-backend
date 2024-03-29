# infraestructura/adaptador_firestore.py
from google.cloud import datastore
import uuid
from datetime import datetime
from pda.modulos.transacciones.dominio.entidades import Transaccion, TransaccionRepository
import firebase_admin
from firebase_admin import credentials
import os


class FirestoreTransaccionRepository(TransaccionRepository):
    def __init__(self):
        # Initialize Firestore client
        self.creds = None 
        self.client = self.inicializar_firebase()
        

    def add(self, transaccion: Transaccion):
        # Convert Transaccion object to dictionary
        transaccion_dict = {
            "id_propiedad": transaccion.id_propiedad,
            "nombre_tomador": transaccion.nombre_tomador,
            "nombre_propietario": transaccion.nombre_propietario,
            "id_transaccion": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat()
        }

        # Add to Firestore (consider handling exceptions and validations)
        key = self.client.key('transacciones')
        transaction_ref = datastore.Entity(key=key)
        transaction_ref.update(transaccion_dict)
        self.client.put(transaction_ref)
        return transaccion_dict
    
    def get(self, transaccion_id: str):
        
        key_transaccion = self.client.key('transacciones', int(transaccion_id))
        transaccion = self.client.get(key_transaccion)
        print(transaccion)
        transaccion_dict = {
            "id_propiedad": transaccion['id_propiedad'],
            "nombre_tomador": transaccion['nombre_tomador'],
            "nombre_propietario": transaccion['nombre_propietario'],
            "timestamp": transaccion['timestamp']
        }
        return transaccion_dict

    def inicializar_firebase(self):
        try:
            # Ruta al archivo de credenciales de Firebase
            credentials_path = 'firebase.json'

            return datastore.Client.from_service_account_json(credentials_path)
        except Exception as e:
            print("Failed to initialize Firebase:", str(e))
