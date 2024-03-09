from dataclasses import dataclass, field
from pda_propiedades_command.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class InformacionGeoespacialDTO(DTO):
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    departamento: str = field(default_factory=str)
    pais: str = field(default_factory=str)


@dataclass(frozen=True)
class InformacionCompaniaDTO(DTO):
    nombre_propietario: str = field(default_factory=str)
    nit: str = field(default_factory=str)
    telefono: str = field(default_factory=str)

@dataclass(frozen=True)
class InformacionContractualDTO(DTO):
    fotografias: list = field(default_factory=list)

@dataclass(frozen=True)
class InformacionCatastralDTO(DTO):
    tipo: str = field(default_factory=str)
    tamano: str = field(default_factory=str)
    tipo_construccion: str = field(default_factory=str)
    numero_pisos: str = field(default_factory=str)

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    informacion_geoespacial: InformacionGeoespacialDTO = field(default_factory=InformacionGeoespacialDTO)
    informacion_compania: InformacionCompaniaDTO = field(default_factory=InformacionCompaniaDTO)
    informacion_contractual: InformacionContractualDTO = field(default_factory=InformacionContractualDTO)
    informacion_catastral: InformacionCatastralDTO = field(default_factory=InformacionCatastralDTO)
    id_transaccion: str = field(default_factory=str)