from routes import page
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask('__name__')
    app.register_blueprint(page)
    return app


my_app = create_app()
