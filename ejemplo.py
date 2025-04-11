"""
Cristian Alexei Romero Martinez
Código de Python
Ingeniería en Sistemas Computacionales

Servidor Web
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index (2).html")

if __name__ == '__main__':
    app.run(debug=True)
