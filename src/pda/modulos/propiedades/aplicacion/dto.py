from dataclasses import dataclass, field
from pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class InformacionGeoespacialDTO(DTO):
    direccion: str
    ciudad: str
    departamento: str
    pais: str


@dataclass(frozen=True)
class InformacionCompaniaDTO(DTO):
    nombre_propietario: str
    nit: str
    telefono: str

@dataclass(frozen=True)
class InformacionContractualDTO(DTO):
    fotografias: list

@dataclass(frozen=True)
class InformacionCatastralDTO(DTO):
    tipo: str
    tamano: str
    tipo_construccion: str
    numero_pisos: str

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    informacion_geoespacial: InformacionGeoespacialDTO = field(default_factory=dict)
    informacion_compania: InformacionCompaniaDTO = field(default_factory=dict)
    informacion_contractual: InformacionContractualDTO = field(default_factory=dict)
    informacion_catastral: InformacionCatastralDTO = field(default_factory=dict)