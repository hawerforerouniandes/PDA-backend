from pda_propiedades_command.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from pda_propiedades_command.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson

from pda_propiedades_command.seedwork.dominio.excepciones import ExcepcionDominio
from pda_propiedades_command.seedwork.presentacion import api
import json
from flask import request
from flask import Response, make_response, jsonify

bp = api.crear_blueprint('propiedad', '/propiedad')

@bp.route('/<id>', methods=('GET',))
def dar_propiedad(id=None):
    if id:
        
        sp = ServicioPropiedad()
        map_propiedad = MapeadorPropiedadDTOJson()
    
        return map_propiedad.dto_a_externo(sp.obtener_propiedad_por_id(id))
    
    else:
        return make_response(jsonify({"error": "ID del contrato no proporcionado"}), 400)
    
