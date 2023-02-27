from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = "sad@#!#@!$@!SD$#$@$#$#$@#sdsadsadsad@#@!#"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ta7nguyenphuocvu@localhost/labsaledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8
app.config['COMMENT_SIZE'] = 10

db = SQLAlchemy(app=app)

cloudinary.config(
    cloud_name = 'ta7nguyenphuocvu',
    api_key = '168711479221251',
    api_secret = 'EjTJgC37McJmhLYHTmK5gK9JGiY',
)

login = LoginManager(app=app)

