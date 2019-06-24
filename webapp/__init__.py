from flask import Flask
from flask.cli import AppGroup
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()

db_cli = AppGroup('db')


@db_cli.command('create')
def create_models():
    db.create_all()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    app.config.from_pyfile('config.py')
    app.config.from_envvar('APP_CONFIG_FILE')

    db.init_app(app)
    # noinspection PyTypeChecker
    api.init_app(app)

    app.cli.add_command(db_cli)

    return app
