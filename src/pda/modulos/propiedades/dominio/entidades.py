"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""
from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID

from pda.modulos.propiedades.dominio.eventos import PropiedadCreada
from pda.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class InformacionGeoespacial(Entidad):
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    departamento: str  = field(default_factory=str)
    pais: str = field(default_factory=str)


@dataclass
class InformacionCompania(Entidad):
    nombre_propietario: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    telefono: str = field(default_factory=str)

@dataclass
class InformacionContractual(Entidad):
    fotografias: list = field(default_factory=list)

@dataclass
class InformacionCatastral(Entidad):
    tipo: str = field(default_factory=str)
    tamano: str = field(default_factory=str)
    tipo_construccion: str = field(default_factory=str)
    numero_pisos: str = field(default_factory=str)

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: str = field(default=None)
    nombre: str = field(default=None)
    informacion_catastral: InformacionCatastral = field(default_factory=InformacionCatastral)
    informacion_contractual: InformacionContractual = field(default_factory=InformacionContractual)
    informacion_geoespacial: InformacionGeoespacial = field(default_factory=InformacionGeoespacial)
    informacion_compania: InformacionCompania = field(default_factory=InformacionCompania)
    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propiedad  = propiedad.id_propiedad
        self.agregar_evento(PropiedadCreada(id_propiedad=self.id, fecha_creacion=self.fecha_creacion))