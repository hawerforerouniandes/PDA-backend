from dataclasses import dataclass, field

from pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class TomadorDTO(DTO):
    nombre: str
    # TODO Convertir a objeto valor
    tipo_documento: str
    documento: str
    telefono: str
    fecha_inicio: str
    fecha_fin: str

@dataclass(frozen=True)
class TransaccionDTO(DTO):
    id_propiedad: field(default_factory=str)
    tomador: field(default_factory=TomadorDTO)
    # Convertir a objeto valor
    tipo_transaccion: field(default_factory=str)