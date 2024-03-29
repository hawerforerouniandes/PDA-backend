"""Entidades del dominio de transacciones

En este archivo usted encontrará las entidades del dominio de transacciones

"""
from dataclasses import dataclass, field

from pda_transacciones_query.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Transaccion(AgregacionRaiz):
    id_propiedad: str = field(default_factory=str)
    nombre_tomador: str = field(default_factory=str)
    nombre_propietario: str = field(default_factory=str)
    id_transaccion: str =  field(default_factory=str)


class TransaccionRepository:
    def add(self, transaccion: Transaccion):
        raise NotImplementedError
    
    def get(self, id_transaccion: str) -> Transaccion:
        raise NotImplementedError

