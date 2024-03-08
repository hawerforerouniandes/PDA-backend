from pulsar.schema import String

from pda_propiedades_query.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class TransaccionAsignadaPayload(ComandoIntegracion):
    id_propiedad = String()
    nombre_tomador = String()
    nombre_propietario = String()


class EventoTransaccionAsignada(ComandoIntegracion):
    data = TransaccionAsignadaPayload()