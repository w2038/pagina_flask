from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['wagner', 'lorena', 'max', 'vinicius']

app.config['SECRET_KEY'] = '35ce51c3d16aaab432353076fe5c35d4'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)