from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.models import Descuento, Categoria

descuento_bp = Blueprint('descuentos', __name__)

@descuento_bp.route('/')
def listar_descuentos():
    descuentos = Descuento.query.all()
    return render_template('index.html', descuentos=descuentos)

@descuento_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_descuento():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nombre_producto = request.form['nombre_producto']
        descripcion = request.form['descripcion']
        precio_original = float(request.form['precio_original'])
        precio_descuento = float(request.form['precio_descuento'])
        categoria_id = request.form.get('categoria_id') or None

        nuevo = Descuento(
            nombre_producto=nombre_producto,
            descripcion=descripcion,
            precio_original=precio_original,
            precio_descuento=precio_descuento,
            categoria_id=categoria_id
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('descuentos.listar_descuentos'))
    return render_template('form.html', categorias=categorias)

@descuento_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_descuento(id):
    descuento = Descuento.query.get_or_404(id)
    categorias = Categoria.query.all()
    if request.method == 'POST':
        descuento.nombre_producto = request.form['nombre_producto']
        descuento.descripcion = request.form['descripcion']
        descuento.precio_original = float(request.form['precio_original'])
        descuento.precio_descuento = float(request.form['precio_descuento'])
        descuento.categoria_id = request.form.get('categoria_id') or None
        db.session.commit()
        return redirect(url_for('descuentos.listar_descuentos'))
    return render_template('form.html', descuento=descuento, categorias=categorias)

@descuento_bp.route('/eliminar/<int:id>')
def eliminar_descuento(id):
    descuento = Descuento.query.get_or_404(id)
    db.session.delete(descuento)
    db.session.commit()
    return redirect(url_for('descuentos.listar_descuentos'))
