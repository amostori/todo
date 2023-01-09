import os

from routes import page
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def create_app():
    app = Flask('__name__')
    client = MongoClient(os.environ.get('MONGO_DB'))
    app.db = client.get_default_database()
    app.register_blueprint(page)
    return app


my_app = create_app()
