from flask import Flask, request, Blueprint
from .items.controller import items
from .extension import db, ma
from .model import Items 
import os
from .swagger.swagger import SWAGGERUI_BLUEPRINT 

def create_db(app):
    if not os.path.exists("/lib/item.db"):
        with app.app_context():
            db.create_all()
            print("Creating DB...")


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(items)    
    app.register_blueprint(SWAGGERUI_BLUEPRINT)
    return app