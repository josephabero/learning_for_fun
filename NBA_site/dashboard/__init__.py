from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SECRET_KEY"] = "687290f23c02b57a075d51f65ed35446"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# db = SQLAlchemy(app)

# Avoids circular import
from dashboard import routes