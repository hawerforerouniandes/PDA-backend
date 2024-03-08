""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""
from dataclasses import dataclass

from pda.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioTransacciones
from pda.modulos.propiedades.infraestructura.repositorios import FirestorePropiedadRepository
from pda.modulos.transacciones.infraestructura.adaptador_firestore import FirestoreTransaccionRepository
from pda.seedwork.dominio.excepciones import ExcepcionFabrica
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return FirestorePropiedadRepository()
        else:
            raise ExcepcionFabrica()