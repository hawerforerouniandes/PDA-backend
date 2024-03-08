from pda_transacciones_query.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from pda_transacciones_query.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pda_transacciones_query.seedwork.aplicacion.comandos import ComandoHandler


class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
