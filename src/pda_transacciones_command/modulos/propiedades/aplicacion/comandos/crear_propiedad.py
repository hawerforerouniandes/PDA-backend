from dataclasses import dataclass

from pda_transacciones_command.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from pda_transacciones_command.modulos.propiedades.dominio.entidades import Propiedad
from pda_transacciones_command.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from pda_transacciones_command.seedwork.aplicacion.comandos import ejecutar_commando as comando

from pda_transacciones_command.modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from pda_transacciones_command.modulos.propiedades.aplicacion.dto import InformacionGeoespacialDTO, InformacionCompaniaDTO, \
    InformacionContractualDTO, InformacionCatastralDTO, PropiedadDTO
from pda_transacciones_command.seedwork.aplicacion.comandos import Comando
from pda_transacciones_command.seedwork.infraestructura.uow import UnidadTrabajoPuerto


@dataclass
class CrearPropiedad(Comando):
    id: str
    nombre: str
    fecha_creacion: str
    fecha_actualizacion: str
    informacion_geoespacial: InformacionGeoespacialDTO
    informacion_compania: InformacionCompaniaDTO
    informacion_contractual: InformacionContractualDTO
    informacion_catastral: InformacionCatastralDTO

class CrearPropiedadHandler(CrearPropiedadBaseHandler):

    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(id=comando.id, nombre=comando.nombre,
                                     fecha_creacion=comando.fecha_creacion, fecha_actualizacion=comando.fecha_actualizacion,
                                     informacion_geoespacial=comando.informacion_geoespacial, informacion_compania=comando.informacion_compania,
                                     informacion_contractual=comando.informacion_contractual, informacion_catastral=comando.informacion_catastral)

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)


