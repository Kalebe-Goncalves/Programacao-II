from flask import Flask, render_template, request, redirect ,url_for, session
#import das operações feitas no bd
import bd_pi as bd
# Obs: Importante executar o bd antes de rodar o servidor


app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste'

#rota inicial/principal 
@app.route("/")
def inicio():
    #listas necessarias para listar as noticias
    lista_tit = bd.listar_noticia_tit()
    lista_text = bd.listar_noticia_text()
    lista_aut = bd.listar_noticia_autor()
    #mostra o site principal passando as listas necessarias
    return render_template("pi2019.html", lista_noticias = lista_tit, lista_noticias_info = lista_text, lista_noticias_autor = lista_aut)

@app.route("/desenv")
def desenv():
    return render_template("desenvolvedores.html")

@app.route("/form_login")
def form_login():
    return render_template("login.html")

#faz a verificacao do login
@app.route("/login", methods = ['GET', 'POST'])
def login():
    """
    Resumidamente são pegos os valores digitados e comparados com os valores das listas retornadas pelo bd
    """
    login = request.form["login"]
    senha_usuario = request.form["senha"]
    lista_usuarios_nome = bd.listar_usuarios_nome()
    lista_usuarios_senha = bd.listar_usuarios_senha()
    for nome in lista_usuarios_nome:
        if nome == login:
            for senha in lista_usuarios_senha:
                if senha_usuario == senha:
                    if senha_usuario == "gremio123" and login == "GrêmioIFCBlumenau":
                        session['usuario'] = login
                        return redirect("/")
                    else:
                        session['usuario'] = login
                        return redirect("/")
    return redirect("/form_login")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_usuario", methods = ['GET', 'POST'])
def cadastrar_usuario():
    email = request.form["email"]
    nome_usuario = request.form["nome_usuario"]
    matricula = request.form["matricula"]
    senha = request.form["senha"]
    #chama a funcao para inserir o usuario
    verificador = bd.inserir_usuario("0", nome_usuario, senha, email, matricula)
    if verificador:
        return redirect("/form_login")

@app.route("/incluir_noticia", methods = ['GET', 'POST'])
def incluir_noticia():
    titulo = request.form["titulo"]
    noticia = request.form["noticia"]
    #o autor sera sempre que estiver logado na conta do gremio
    autor = session['usuario']
    print(autor)
    #chama a funcao para incluir a noticia
    verificador = bd.inserir_noticia(titulo, noticia, autor)
    if verificador:
        return redirect("/")

app.run(debug=True)