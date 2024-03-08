""" Fábricas para la creación de objetos del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de propiedades

"""
from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from pda.seedwork.dominio.repositorios import Mapeador, Repositorio
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

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
