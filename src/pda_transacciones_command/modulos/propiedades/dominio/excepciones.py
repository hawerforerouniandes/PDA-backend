""" Excepciones del dominio de propiedades

En este archivo usted encontrará los Excepciones relacionadas
al dominio de propiedades

"""

from pda_transacciones_command.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPropiedadesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de propiedades'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)