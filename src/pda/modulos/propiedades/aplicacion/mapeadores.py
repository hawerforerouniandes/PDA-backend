from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO, InformacionGeoespacialDTO, InformacionCompaniaDTO, InformacionContractualDTO, InformacionCatastralDTO

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        fecha_creacion = externo.get('fecha_creacion')
        fecha_actualizacion = externo.get('fecha_creacion')
        nombre = externo.get('nombre')
        informacion_geoespacial = externo.get('informacion_geoespacial')
        informacion_compania = externo.get('informacion_compania')
        informacion_contractual = externo.get('informacion_contractual')
        informacion_catastral = externo.get('informacion_catastral')

        return PropiedadDTO(fecha_creacion, fecha_actualizacion, "", nombre, informacion_geoespacial, informacion_compania, informacion_contractual, informacion_catastral)

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _nombre = str(entidad.nombre)
        _informacion_geoespacial = InformacionGeoespacialDTO(entidad.informacion_geoespacial)
        _informacion_compania = InformacionCompaniaDTO(entidad.informacion_compania)
        _informacion_contractual = InformacionContractualDTO(entidad.informacion_contractual)
        _informacion_catastral = InformacionCatastralDTO(entidad.informacion_catastral)
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, _nombre, _informacion_geoespacial, _informacion_compania, _informacion_contractual, _informacion_catastral )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.nombre = dto.nombre
        propiedad.informacion_geoespacial = dto.informacion_geoespacial
        propiedad.informacion_compania = dto.informacion_compania
        propiedad.informacion_contractual = dto.informacion_contractual
        propiedad.informacion_catastral = dto.informacion_catastral
        return propiedad