from pda_transacciones_query.seedwork.aplicacion.dto import Mapeador as AppMap
from pda_transacciones_query.seedwork.dominio.repositorios import Mapeador as RepMap
from pda_transacciones_query.modulos.propiedades.dominio.entidades import Propiedad
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
        return PropiedadDTO("",nombre= nombre, fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, informacion_geoespacial=informacion_geoespacial, informacion_compania=informacion_compania, informacion_contractual= informacion_contractual, informacion_catastral=informacion_catastral)

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        print("EntidadPropiedad: ", entidad)
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _id_propiedad = str(entidad.id_propiedad)
        _nombre = str(entidad.nombre)
        _igeo = entidad.informacion_geoespacial
        _icom = entidad.informacion_compania
        _icon = entidad.informacion_contractual
        _icat = entidad.informacion_catastral
        _informacion_geoespacial = InformacionGeoespacialDTO(_igeo.get('direccion'), _igeo.get('ciudad'), _igeo.get('departamento'), _igeo.get('pais'))
        _informacion_compania = InformacionCompaniaDTO(_icom.get('nombre_propietario'), _icom.get('nit'), _icom.get('telefono'))
        _informacion_contractual = InformacionContractualDTO(_icon.get('fotografias'))
        _informacion_catastral = InformacionCatastralDTO(_icat.get('tipo'), _icat.get('tamano'), _icat.get('tipo_construccion'), _icat.get('numero_pisos'))
        return PropiedadDTO(fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, id=_id, nombre=_nombre, informacion_geoespacial=_informacion_geoespacial, informacion_compania=_informacion_compania, informacion_contractual=_informacion_contractual, informacion_catastral=_informacion_catastral, id_propiedad=_id_propiedad )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        print(dto)
        propiedad = Propiedad()
        propiedad.id_propiedad = dto.id_propiedad
        propiedad.nombre = dto.nombre
        propiedad.informacion_geoespacial = dto.informacion_geoespacial
        propiedad.informacion_compania = dto.informacion_compania
        propiedad.informacion_contractual = dto.informacion_contractual
        propiedad.informacion_catastral = dto.informacion_catastral
        return propiedad

    def obtener_tipo(self) -> type:
        return Propiedad.__class__