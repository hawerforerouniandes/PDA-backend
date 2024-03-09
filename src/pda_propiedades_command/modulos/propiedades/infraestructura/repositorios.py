""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedades

"""
from uuid import UUID

from google.cloud import datastore
from pda_propiedades_command.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad

from pda_propiedades_command.modulos.propiedades.dominio.entidades import Propiedad, InformacionGeoespacial, \
    InformacionCompania, InformacionContractual, InformacionCatastral
from pda_propiedades_command.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from pda_propiedades_command.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioTransacciones
from pda_propiedades_command.modulos.transacciones.dominio.entidades import Transaccion


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

    def obtener_por_id(self, id: str) -> Propiedad:
        
        key_propiedad = self.client.key('propiedades', int(id))
        propiedadFirebase = self.client.get(key_propiedad)
        print(propiedadFirebase)

        propiedad = Propiedad()
        informacion_geoespacial_firebase = propiedadFirebase['informacion_geoespacial']
        informacion_geoespacial = InformacionGeoespacial()
        informacion_geoespacial.ciudad = informacion_geoespacial_firebase.get('ciudad')
        informacion_geoespacial.departamento = informacion_geoespacial_firebase.get('departamento')
        informacion_geoespacial.direccion = informacion_geoespacial_firebase.get('direccion')
        informacion_geoespacial.pais = informacion_geoespacial_firebase.get('pais')

        informacion_compania_firebase = propiedadFirebase['informacion_compania']
        informacion_compania = InformacionCompania()
        informacion_compania.nit = informacion_compania_firebase.get('nit')
        informacion_compania.nombre_propietario = informacion_compania_firebase.get('nombre_propietario')
        informacion_compania.telefono = informacion_compania_firebase.get('telefono')

        informacion_contractual_firebase = propiedadFirebase['informacion_contractual']
        informacion_contractual = InformacionContractual()
        informacion_contractual.fotografias = informacion_contractual_firebase.get('fotografias')

        informacion_catastral_firebase = propiedadFirebase['informacion_catastral']
        informacion_catastral = InformacionCatastral()
        informacion_catastral.tamano = informacion_catastral_firebase.get('tamano')
        informacion_catastral.tipo = informacion_catastral_firebase.get('tipo')
        informacion_catastral.numero_pisos = informacion_catastral_firebase.get('numero_pisos')
        informacion_catastral.tipo_construccion = informacion_catastral_firebase.get('tipo_construccion')

        propiedad.nombre = propiedadFirebase['nombre']
        propiedad.informacion_geoespacial = informacion_geoespacial
        propiedad.informacion_compania = informacion_compania
        propiedad.informacion_contractual = informacion_contractual
        propiedad.informacion_catastral = informacion_catastral
        propiedad.id_propiedad = str(id)
        propiedad.id_transaccion = propiedadFirebase.get('id_transaccion')
        return propiedad

    def agregar(self, entity: Propiedad):
        # Convert Propiedad object to dictionary
        propiedad_dict = {
            "nombre": entity.nombre,
            "informacion_contractual": {
                "fotografias": entity.informacion_contractual.fotografias
            },
            "informacion_catastral": {
                "numero_pisos": entity.informacion_catastral.numero_pisos,
                "tamano": entity.informacion_catastral.tamano,
                "tipo": entity.informacion_catastral.tipo,
                "tipo_construccion": entity.informacion_catastral.tipo_construccion
            },
            "informacion_geoespacial": {
                "ciudad": entity.informacion_geoespacial.ciudad,
                "departamento": entity.informacion_geoespacial.departamento,
                "direccion": entity.informacion_geoespacial.direccion,
                "pais": entity.informacion_geoespacial.pais
            },
            "informacion_compania": {
                "nit": entity.informacion_compania.nit,
                "nombre_propietario": entity.informacion_compania.nombre_propietario,
                "telefono": entity.informacion_compania.telefono
            }
        }
        # Add to Firestore (consider handling exceptions and validations)
        key = self.client.key('propiedades')
        transaction_ref = datastore.Entity(key=key)
        transaction_ref.update(propiedad_dict)
        self.client.put(transaction_ref)
        entity.id_propiedad = transaction_ref.id
        return entity

    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        key_propiedad = self.client.key('propiedades', int(entity.id_propiedad))
        propiedad_dict = {
            "nombre": entity.nombre,
            "informacion_contractual": {
                "fotografias": entity.informacion_contractual.fotografias
            },
            "informacion_catastral": {
                "numero_pisos": entity.informacion_catastral.numero_pisos,
                "tamano": entity.informacion_catastral.tamano,
                "tipo": entity.informacion_catastral.tipo,
                "tipo_construccion": entity.informacion_catastral.tipo_construccion
            },
            "informacion_geoespacial": {
                "ciudad": entity.informacion_geoespacial.ciudad,
                "departamento": entity.informacion_geoespacial.departamento,
                "direccion": entity.informacion_geoespacial.direccion,
                "pais": entity.informacion_geoespacial.pais
            },
            "informacion_compania": {
                "nit": entity.informacion_compania.nit,
                "nombre_propietario": entity.informacion_compania.nombre_propietario,
                "telefono": entity.informacion_compania.telefono
            },
            "id_transaccion": entity.id_transaccion
        }
        propiedadFirebase = self.client.get(key_propiedad)
        propiedadFirebase.update(propiedad_dict)
        self.client.put(propiedadFirebase)
        return entity

    def eliminar(self, entity_id: UUID):
        raise NotImplementedError