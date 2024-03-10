from pda_propiedades_query.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from pda_propiedades_query.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson

from pda_propiedades_query.seedwork.dominio.excepciones import ExcepcionDominio
from pda_propiedades_query.seedwork.presentacion import api
import json
from flask import request
from flask import Response, make_response, jsonify

bp = api.crear_blueprint('propiedad', '/propiedad')

@bp.route('/<id>', methods=('GET',))
def dar_propiedad(id=None):
    if id:
        try:
            id_int = int(id)
        except ValueError:
            return make_response(jsonify({"error": "El ID proporcionado no es válido"}), 400)
        
        sp = ServicioPropiedad()
        map_propiedad = MapeadorPropiedadDTOJson()
    
        return map_propiedad.dto_a_externo(sp.obtener_propiedad_por_id(id_int))
    
    else:
        return make_response(jsonify({"error": "ID del contrato no proporcionado"}), 400)