from pda_transacciones_command.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion
from pulsar.schema import *

class AsignarTransaccionPayload(ComandoIntegracion):
    id_propiedad = String()
    nombre_tomador = String()
    nombre_propietario = String()

class ComandoAsignarTransaccion(ComandoIntegracion):
    data = AsignarTransaccionPayload()