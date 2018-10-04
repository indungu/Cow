import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db,APP
from models import model

migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db',MigrateCommand)


if __name__ =='__main__':
    manager.run()