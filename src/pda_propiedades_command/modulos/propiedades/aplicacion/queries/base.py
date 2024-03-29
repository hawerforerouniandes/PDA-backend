from pda_propiedades_command.seedwork.aplicacion.queries import QueryHandler
from pda_propiedades_command.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pda_propiedades_command.modulos.propiedades.dominio.fabricas import FabricaPropiedades

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_propiedades