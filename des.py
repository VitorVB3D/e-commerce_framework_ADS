from flask import Flask

from flask import render_template



app = Flask(__name__)

@app.route("/") # Está chamando uma pagina HTML 
def index():
    return render_template('index.html')

@app.route("/login")
def sobre():
    return render_template('login.html')


@app.route("/categorias")
def categorias():
    return render_template('categorias.html')

@app.route("/categorias/lcds")
def lcds():
    return render_template('lcds.html')

@app.route("/ofertas")
def ofertas():
    return render_template('ofertas.html')

@app.route("/ofertas/produto")
def ofertas_prod():
    return render_template('produto.html')

    


