from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_api
from api.model import db

api = create_api()

migrate = Migrate(api, db)
manager = Manager(api)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()