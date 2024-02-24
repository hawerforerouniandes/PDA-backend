"""Entidades del dominio de transacciones

En este archivo usted encontrará las entidades del dominio de transacciones

"""
from dataclasses import dataclass, field

from pda.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Tomador(Entidad):
    nombre: str = field(default_factory=str)
    # TODO Convertir a objeto valor
    tipo_documento: str = field(default_factory=str)
    documento: str = field(default_factory=str)
    telefono: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)
@dataclass
class Transaccion(AgregacionRaiz):
    id_propiedad: str = field(default_factory=str)
    tomador: Tomador = field(default_factory=Tomador)
    # TODO Convertir a objeto valor
    tipo_transaccion: str = field(default_factory=str)