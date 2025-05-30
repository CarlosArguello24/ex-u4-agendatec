from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importar modelos y blueprints
from app.models.models import Descuento, Categoria
from app.routes.descuento import descuento_bp

with app.app_context():
    db.create_all()

app.register_blueprint(descuento_bp, url_prefix='/descuentos')

@app.route('/')
def index():
    return render_template('index.html', descuentos=Descuento.query.all())
