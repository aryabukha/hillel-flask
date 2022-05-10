from flask import Flask

import config

app = Flask(__name__, template_folder='template')
app.config.from_object(config.Config)

from app import routes