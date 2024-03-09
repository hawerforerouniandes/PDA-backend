from pda_propiedades_command.seedwork.aplicacion.servicios import Servicio
from pda_propiedades_command.modulos.propiedades.dominio.entidades import Propiedad
from pda_propiedades_command.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from pda_propiedades_command.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pda_propiedades_command.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from pda_propiedades_command.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .handlers import HandlerPropiedadIntegracion
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO
from ...transacciones.aplicacion.dto import TransaccionDTO
from ...transacciones.dominio.entidades import Transaccion


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
        repositorio.agregar(propiedad)
        # UOW Añadir
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()
        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    def asignar_transaccion(self, transaccion_dto: TransaccionDTO) -> TransaccionDTO:
        HandlerPropiedadIntegracion.handle_asignar_transaccion(transaccion_dto)
        HandlerPropiedadIntegracion.handle_publicar_sagalog(transaccion_dto, 'asignar-transaccion','evento-enviado','propiedades-command','normal')
        return transaccion_dto

    def actualizar_propiedad_con_transaccion(self, transaccion: TransaccionDTO):
        propiedad_dto: PropiedadDTO = self.obtener_propiedad_por_id(transaccion.id_propiedad)
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.id_transaccion = transaccion.id_transaccion
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.actualizar(propiedad)
        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
    
    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

    