import pathlib

# import connexion
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent.resolve()
# connex_app = connexion.App(__name__, specification_dir=basedir)

app = Flask(__name__, instance_relative_config=False)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'ebooksharing.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)
