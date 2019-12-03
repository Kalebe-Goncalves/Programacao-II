from flask import Flask, render_template, request, redirect , url_for
from salvar_consultar_BD import listar_roupas 

roupas = listar_roupas()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/loja")
def loja():
    return render_template("lojaFeminina_compras.html")

@app.route("/loja2")
def loja2():
    return render_template("lojaFeminina_compras2.html")


app.run(debug=True)