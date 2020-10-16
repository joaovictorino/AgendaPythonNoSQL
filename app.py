import configparser
import common
from flask import Flask
app = Flask(__name__)

common.app = app

config = configparser.ConfigParser()
config.read('config.ini')
common.config = config

import agenda.presentation.controller.agendaController

if __name__ == "__main__":
    app.run()