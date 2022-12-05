from flask import Flask
from  config import Config
from flask_migrate import Migrate #type:ignore
from .models import db #type:ignore
from .auth.routes import auth
app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models