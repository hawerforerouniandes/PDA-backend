from pda_propiedades_command.seedwork.aplicacion.dto import Mapeador as AppMap
from pda_propiedades_command.seedwork.dominio.repositorios import Mapeador as RepMap
from pda_propiedades_command.modulos.propiedades.dominio.entidades import Propiedad, InformacionGeoespacial, \
    InformacionCompania, InformacionContractual, InformacionCatastral
from .dto import PropiedadDTO, InformacionGeoespacialDTO, InformacionCompaniaDTO, InformacionContractualDTO, InformacionCatastralDTO
from ...transacciones.aplicacion.dto import TransaccionDTO
from ...transacciones.dominio.entidades import Transaccion


class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        fecha_creacion = externo.get('fecha_creacion')
        fecha_actualizacion = externo.get('fecha_creacion')
        nombre = externo.get('nombre')
        _igeo = externo.get('informacion_geoespacial')
        _icom = externo.get('informacion_compania')
        _icon = externo.get('informacion_contractual')
        _icat = externo.get('informacion_catastral')
        _informacion_geoespacial = InformacionGeoespacialDTO(_igeo.get('direccion'), _igeo.get('ciudad'), _igeo.get('departamento'),
                                                             _igeo.get('pais'))
        _informacion_compania = InformacionCompaniaDTO(_icom.get('nombre_propietario'), _icom.get('nit'), _icom.get('telefono'))
        _informacion_contractual = InformacionContractualDTO(_icon.get('fotografias'))
        _informacion_catastral = InformacionCatastralDTO(_icat.get('tipo'), _icat.get('tamano'), _icat.get('tipo_construccion'),
                                                         _icat.get('numero_pisos'))
        return PropiedadDTO(nombre= nombre, fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, informacion_geoespacial=_informacion_geoespacial, informacion_compania=_informacion_compania, informacion_contractual= _informacion_contractual, informacion_catastral=_informacion_catastral)

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _id_propiedad = str(entidad.id_propiedad)
        _nombre = str(entidad.nombre)
        _igeo = entidad.informacion_geoespacial
        _icom = entidad.informacion_compania
        _icon = entidad.informacion_contractual
        _icat = entidad.informacion_catastral
        _informacion_geoespacial = InformacionGeoespacialDTO(_igeo.direccion, _igeo.ciudad, _igeo.departamento, _igeo.pais)
        _informacion_compania = InformacionCompaniaDTO(_icom.nombre_propietario, _icom.nit, _icom.telefono)
        _informacion_contractual = InformacionContractualDTO(_icon.fotografias)
        _informacion_catastral = InformacionCatastralDTO(_icat.tipo, _icat.tamano, _icat.tipo_construccion, _icat.numero_pisos)
        _id_transaccion = str(entidad.id_transaccion)
        return PropiedadDTO(fecha_creacion=fecha_creacion, fecha_actualizacion=fecha_actualizacion, id=_id, nombre=_nombre, informacion_geoespacial=_informacion_geoespacial, informacion_compania=_informacion_compania, informacion_contractual=_informacion_contractual, informacion_catastral=_informacion_catastral, id_propiedad=_id_propiedad, id_transaccion=_id_transaccion )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.id_propiedad = dto.id_propiedad
        propiedad.nombre = dto.nombre
        _informacion_geoespacial = InformacionGeoespacial(direccion=dto.informacion_geoespacial.direccion, ciudad=dto.informacion_geoespacial.ciudad,
                                                          departamento=dto.informacion_geoespacial.departamento, pais=dto.informacion_geoespacial.pais)
        _informacion_compania = InformacionCompania(nombre_propietario=dto.informacion_compania.nombre_propietario, nit=dto.informacion_compania.nit,
                                                    telefono=dto.informacion_compania.telefono)
        _informacion_contractual = InformacionContractual(fotografias=dto.informacion_contractual.fotografias)
        _informacion_catastral = InformacionCatastral(tipo=dto.informacion_catastral.tipo, tamano=dto.informacion_catastral.tamano,
                                                      tipo_construccion=dto.informacion_catastral.tipo_construccion, numero_pisos=dto.informacion_catastral.numero_pisos)
        propiedad.informacion_geoespacial = _informacion_geoespacial
        propiedad.informacion_compania = _informacion_compania
        propiedad.informacion_contractual = _informacion_contractual
        propiedad.informacion_catastral = _informacion_catastral
        propiedad.id_transaccion = dto.id_transaccion
        return propiedad

    def obtener_tipo(self) -> type:
        return Propiedad.__class__