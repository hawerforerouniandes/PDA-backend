from pda_transacciones_query.modulos.transacciones.aplicacion.servicio_transaccion import ServicioTransaccion
from pda_transacciones_query.modulos.transacciones.aplicacion.mapeadores import MapeadorTransaccionDTOJson

from pda_transacciones_query.seedwork.dominio.excepciones import ExcepcionDominio
from pda_transacciones_query.seedwork.presentacion import api
import json
from flask import request
from flask import Response, make_response, jsonify

bp = api.crear_blueprint('transacciones', '/transacciones')

@bp.route('/<id>', methods=('GET',))
def dar_contrato(id=None):
    if id:
        st = ServicioTransaccion()
        return st.obtener_transaccion_por_id(id)
    else:
        return make_response(jsonify({"error": "ID del contrato no proporcionado"}), 400)
