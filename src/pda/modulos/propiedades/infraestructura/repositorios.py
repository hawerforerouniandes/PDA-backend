""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedades

"""
from uuid import UUID

from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioTransacciones
from pda.modulos.transacciones.dominio.entidades import Transaccion


class RepositorioPropiedadesSQL(RepositorioPropiedades):

    def obtener_por_id(self, id: UUID) -> Propiedad:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def asignar_transaccion(self, entity: Transaccion):
        # TODO
        raise NotImplementedError