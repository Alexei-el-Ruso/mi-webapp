"""
    Cristian Alexei Romero Martinez
    Código de Python
    Ingeniería en Sistemas Computacionales

    Servidor Web
"""

from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

catalogo = [
    {"ID": 1, "Nombre":"Pan",		"Precio": 10,	"Inventario": 0},
    {"ID": 2, "Nombre":"Huevo",		"Precio": 30,	"Inventario": 0},
    {"ID": 3, "Nombre":"Fruta",		"Precio": 8,	"Inventario": 0},
    {"ID": 4, "Nombre":"Lorem",		"Precio": 15,	"Inventario": 0},
    {"ID": 5, "Nombre":"Ipsum",		"Precio": 17,	"Inventario": 0},
    {"ID": 6, "Nombre":"Dolor",		"Precio": 100,	"Inventario": 0},
    {"ID": 7, "Nombre":"Pilas AAA",	"Precio": 46,	"Inventario": 0},
    {"ID": 8, "Nombre":"Pilas AA",	"Precio": 98,	"Inventario": 0},
    {"ID": 9, "Nombre":"Pilas A",	"Precio": 68,	"Inventario": 0},
    {"ID": 10, "Nombre":"Pilas B",	"Precio": 6,	"Inventario": 0},
    {"ID": 11, "Nombre":"Pilas C",	"Precio": 86,	"Inventario": 0},
    {"ID": 12, "Nombre":"Pilas D",	"Precio": 76,	"Inventario": 0}
]

@app.route('/')
def home():
	print("Catálogo:")
	for i in catalogo:
		print(i)
	return render_template("index.html", productos=catalogo)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/agregar/<id>')
def agregar_carrito(id):
    if 'carrito' not in session:
        session['carrito'] = []
    session['carrito'].append(id)
    session.modified = True
    return redirect(url_for('home'))
