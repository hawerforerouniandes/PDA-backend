""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedades

"""
from uuid import UUID

from google.cloud import datastore

from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from pda.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioTransacciones
from pda.modulos.transacciones.dominio.entidades import Transaccion


class FirestorePropiedadRepository(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()
        self.creds = None
        self.client = self.inicializar_firebase()

    def inicializar_firebase(self):
        try:
            # Ruta al archivo de credenciales de Firebase
            credentials_path = 'firebase.json'

            return datastore.Client.from_service_account_json(credentials_path)
        except Exception as e:
            print("Failed to initialize Firebase:", str(e))

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Propiedad):
        # Convert Propiedad object to dictionary
        propiedad_dict = {
            "nombre": entity.nombre,
            "informacion_contractual": entity.informacion_contractual,
            "informacion_catastral": entity.informacion_catastral,
            "informacion_geoespacial": entity.informacion_geoespacial,
            "informacion_compania": entity.informacion_compania
        }
        # Add to Firestore (consider handling exceptions and validations)
        key = self.client.key('propiedades')
        transaction_ref = datastore.Entity(key=key)
        transaction_ref.update(propiedad_dict)
        self.client.put(transaction_ref)
        print("Propiedad a Persistir: ", propiedad_dict)
        return entity

    def asignar_transaccion(self, entity: Transaccion):
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError