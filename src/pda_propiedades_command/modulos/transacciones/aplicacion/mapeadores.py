from pda_propiedades_command.modulos.transacciones.aplicacion.dto import TransaccionDTO
from pda_propiedades_command.modulos.transacciones.dominio.entidades import Transaccion
from pda_propiedades_command.seedwork.aplicacion.dto import Mapeador as AppMap
from pda_propiedades_command.seedwork.dominio.repositorios import Mapeador as RepMap

class MapeadorTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: any) -> TransaccionDTO:
        print("entro", externo)
        id_propiedad = externo.get('id_propiedad')
        tomador = externo.get('nombre_tomador')
        nombre_propiedario = externo.get('nombre_propietario')
        id_transaccion = externo.get('id_transaccion')
        return TransaccionDTO(id_propiedad=id_propiedad, nombre_tomador=tomador, nombre_propietario=nombre_propiedario, id_transaccion=id_transaccion)

    def dto_a_externo(self, dto: TransaccionDTO) -> any:
        return dto.__dict__


class MapeadorTransaccion(RepMap):

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        _id_propiedad = str(entidad.id_propiedad)
        _id_transaccion = str(entidad.id_transaccion)
        _nombre_tomador = str(entidad.nombre_tomador)
        _nombre_propietario = str(entidad.nombre_propietario)
        return TransaccionDTO(id_propiedad=_id_propiedad, nombre_tomador=_nombre_tomador,
                              nombre_propietario=_nombre_propietario)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion()
        transaccion.id_propiedad = dto.id_propiedad
        transaccion.nombre_tomador = dto.nombre_tomador
        transaccion.nombre_propietario = dto.nombre_propietario
        return transaccion

    def obtener_tipo(self) -> type:
        return Transaccion.__class__


