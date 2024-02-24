bp = api.crear_blueprint()

@bp.route('/propiedad', methods=('POST',))
def crear_propiedad():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        sp = ServicioPropiedad()
        dto_final = sp.crear_propiedad(propiedad_dto)
        return map_propiedad.dto_a_externo(dto_final)

    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad/transaccion', methods=('POST',))
def asignar_transaccion():
    try:
        transaccion_dict = request.json
        map_transaccion = MapeadorTransaccionDTOJson()
        transaccion_dto = map_transaccion.externo_a_dto(transaccion_dict)

        sp = ServicioTransaccion()
        dto_final = sp.asignar_transaccion(transaccion_dto)
        return map_transaccion.dto_a_externo(dto_final)

    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
