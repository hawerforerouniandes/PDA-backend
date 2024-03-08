from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from pda_transacciones_query.seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: str = None
    id_propietario: str = None
    fecha_creacion: datetime = None

@dataclass
class AsignarTransaccion(EventoDominio):
    id_propiedad: str = None
    nombre_tomador: str = None
    nombre_propietario: str =None