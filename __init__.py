from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'group8'

from Major_Project_Flask import routes