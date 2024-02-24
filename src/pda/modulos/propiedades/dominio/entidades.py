"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""
from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID

from pda.modulos.propiedades.dominio.eventos import PropiedadCreada
from pda.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class InformacionGeoespacialDTO(Entidad):
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    departamento: str  = field(default_factory=str)
    pais: str = field(default_factory=str)


@dataclass
class InformacionCompaniaDTO(Entidad):
    nombre_propietario: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    telefono: str = field(default_factory=str)

@dataclass
class InformacionContractualDTO(Entidad):
    fotografias: list = field(default_factory=list)

@dataclass
class InformacionCatastralDTO(Entidad):
    tipo: str = field(default_factory=str)
    tamano: str = field(default_factory=str)
    tipo_construccion: str = field(default_factory=str)
    numero_pisos: str = field(default_factory=str)

@dataclass
class Propiedad(AgregacionRaiz):
    id_propietario: UUID = field(hash=True, default=None)
    nombre: str = field(default=None)
    informacion_catastral: InformacionCatastralDTO = field(default_factory=InformacionCatastralDTO)
    informacion_contractual: InformacionContractualDTO = field(default_factory=InformacionContractualDTO)
    informacion_geoespacial: InformacionGeoespacialDTO = field(default_factory=InformacionGeoespacialDTO)
    informacion_compania: InformacionCompaniaDTO = field(default_factory=InformacionCompaniaDTO)
    def crear_propiedad(self, propiedad: Propiedad):
        self.id_propietario  = propiedad.id_propietario
        self.agregar_evento(PropiedadCreada(id_propiedad=self.id, fecha_creacion=self.fecha_creacion))