import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
import threading
import pda.modulos.propiedades.infraestructura.consumidores as consumidor_propiedades_update

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import pda.modulos.propiedades.infraestructura.dto
    import pda.modulos.transacciones.infraestructura.dto

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from pda.config.db import init_db
    init_db(app)

    from pda.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()
        threading.Thread(target=consumidor_propiedades_update.suscribirse_transacciones_update).start()
        

     # Importa Blueprints
    from . import transacciones
    from . import propiedades

    # Registro de Blueprints
    app.register_blueprint(propiedades.bp)
    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
