from dataclasses import dataclass, field

from src.pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class TransaccionDTO(DTO):
    id_propiedad: field(default_factory=str)
    nombre_tomador: field(default_factory=str)
    # Convertir a objeto valor
    nombre_propiedario: field(default_factory=str)