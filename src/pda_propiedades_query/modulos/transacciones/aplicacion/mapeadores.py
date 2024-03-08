from pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap

class MapeadorTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: any) -> TransaccionDTO:
        print("entro", externo)
        id_propiedad = externo.get('id_propiedad')
        tomador = externo.get('nombre_tomador')
        nombre_propiedario = externo.get('nombre_propietario')
        return TransaccionDTO(id_propiedad, tomador, nombre_propiedario)

    def dto_a_externo(self, dto: TransaccionDTO) -> any:
        return dto.__dict__

class MapeadorTransaccion:
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Transaccion) -> any:
        _id_propiedad = str(entidad.id_propiedad)
        _nombre_tomador = str(entidad.nombre_tomador)
        _nombre_propietario = str(entidad.nombre_propietario)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.nombre_tomador = dto.nombre_tomador
        transaccion.nombre_propietario = dto.nombre_propietario
        return transaccion
