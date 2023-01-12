import os

from routes import page
from htmx_routes import htmx_page
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from db import db

load_dotenv()


def create_app():
    app = Flask('__name__')
    client = MongoClient(os.environ.get('MONGO_DB'))
    app.db = client.get_default_database()

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sqlite.db'
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(page)
    app.register_blueprint(htmx_page)
    return app


my_app = create_app()
