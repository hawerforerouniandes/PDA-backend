from pda.modulos.transacciones.aplicacion.dto import TransaccionDTO, TomadorDTO
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap

class MapeadorTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: any) -> TransaccionDTO:
        id_propiedad = externo.get('id_propiedad')
        tomador = externo.get('tomador')
        tipo_transaccion = externo.get('tipo_transaccion')
        return TransaccionDTO(id_propiedad, tomador, tipo_transaccion)

    def dto_a_externo(self, dto: TransaccionDTO) -> any:
        return dto.__dict__

class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Transaccion) -> any:
        _id_propiedad = str(entidad.id_propiedad)
        _tomador = TomadorDTO(entidad.tomador)
        _tipo_transaccion = str(entidad.tipo_transaccion)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.tomador = dto.tomador
        transaccion.tipo_transaccion = dto.tipo_transaccion
        return transaccion
