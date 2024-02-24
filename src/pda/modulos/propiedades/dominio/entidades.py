"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Propiedad(AgregacionRaiz):
    id_propietario: uuid.UUID = field(hash=True, default=None)
    nombre: str = field(default=None)
    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propietario  = propiedad.id_propietario
        self.agregar_evento(PropiedadCreada(id_propiedad=self.id, fecha_creacion=self.fecha_creacion))
