import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
UPLOADS_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

bootstrap = Bootstrap(app)

from roadrunner import routes