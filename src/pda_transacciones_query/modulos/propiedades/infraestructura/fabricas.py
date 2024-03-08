""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""
from dataclasses import dataclass

from pda_transacciones_query.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioTransacciones
from pda_transacciones_query.modulos.propiedades.infraestructura.repositorios import FirestorePropiedadRepository
from pda_transacciones_query.modulos.transacciones.infraestructura.adaptador_firestore import FirestoreTransaccionRepository
from pda_transacciones_query.seedwork.dominio.excepciones import ExcepcionFabrica
from pda_transacciones_query.seedwork.dominio.fabricas import Fabrica
from pda_transacciones_query.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return FirestorePropiedadRepository()
        else:
            raise ExcepcionFabrica()