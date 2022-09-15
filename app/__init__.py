from flask import Flask
from flask_cors import CORS
from flask_ckeditor import CKEditor

app = Flask(__name__, static_folder='./static', static_url_path='/files')

CKEditor(app)
CORS(app, resources=r'/*')
app.config['SECRET_KEY'] = "newg@secret"
