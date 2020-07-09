from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import create_database, database_exists, drop_database
import pymysql
import connexion
pymysql.install_as_MySQLdb()
import MySQLdb

# Conectando a DB e criando a database, ou deletar e criar caso ela já exista
dburl = 'mysql://{0}:{1}@{2}/student'.format("root", "example", "mysql")
if not database_exists(dburl):
    create_database(dburl)
else:
    drop_database(dburl)
    create_database(dburl)

# criando um connexion application e associando a instancia do Flask
connex_app = connexion.App(__name__)
app = connex_app.app

#trazendo os dados para a DB
app.config['SQLALCHEMY_DATABASE_URI'] = dburl
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Iniciando o Marshmallow para serialização
ma = Marshmallow(app)
