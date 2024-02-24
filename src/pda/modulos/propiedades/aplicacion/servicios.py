from pda.seedwork.aplicacion.servicios import Servicio
from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from pda.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pda.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from pda.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO
from ...transacciones.aplicacion.dto import TransaccionDTO


class ServicioPropiedad(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        # UOW Añadir
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()
        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    