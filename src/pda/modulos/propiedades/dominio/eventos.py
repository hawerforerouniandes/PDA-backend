from __future__ import annotations
from dataclasses import dataclass, field
from pda.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: uuid.UUID = None
    id_propietario: uuid.UUID = None
    fecha_creacion: datetime = None