""" Fábricas para la creación de objetos del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de propiedades

"""
from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from pda_propiedades_command.seedwork.dominio.repositorios import Mapeador, Repositorio
from pda_propiedades_command.seedwork.dominio.fabricas import Fabrica
from pda_propiedades_command.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from pda_propiedades_command.modulos.transacciones.dominio.entidades import Transaccion


@dataclass
class _FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            return propiedad

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedades()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()


@dataclass
class _FabricaTransacciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            transaccion: Transaccion = mapeador.dto_a_entidad(obj)
            return transaccion

@dataclass
class FabricaTransacciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_transaccion = _FabricaTransacciones()
            return fabrica_transaccion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()
