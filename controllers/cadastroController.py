from flask import Blueprint, render_template, request
from flask_login import login_user
import hashlib
from models import Usuario
from db import db

class CadastroController:
    def __init__(self):
        self.blueprint = Blueprint('cadastro', __name__)
        self._add_rotas()

    def hash(self, txt):
        return hashlib.sha256(txt.encode('utf-8')).hexdigest()

    def _add_rotas(self):
        self.blueprint.add_url_rule('/', view_func=self.cadastro, methods=['GET', 'POST'])

    def cadastro(self):
        if request.method == 'GET':
            return render_template('cadastro.html')

        nome = request.form['nomeForm']
        sobrenome = request.form['sobrenomeForm']
        email = request.form['emailForm']
        senha = request.form['senhaForm']

        if not all([nome, sobrenome, email, senha]):
            return "preencha todos os campos"
        elif int(senha) < 5:
            return "senha inválida, mínimo de 5 caracteres"
        else:
            novo_user = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=self.hash(senha))

            db.session.add(novo_user)
            db.session.commit()
            login_user(novo_user)
            return render_template('login.html')