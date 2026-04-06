from flask import Blueprint, render_template, request, url_for
from flask_login import login_user
from werkzeug.utils import redirect
import hashlib
from models import Usuario

class LoginController:
    def __init__(self, login_manager):
        self.login_manager = login_manager
        self.blueprint = Blueprint('login', __name__)
        self._add_rotas()

        @self.login_manager.user_loader
        def load_user(id):
            return Usuario.query.get(id)

    def hash(self, txt):
        return hashlib.sha256(txt.encode('utf-8')).hexdigest()

    def _add_rotas(self):
        self.blueprint.add_url_rule('/', view_func=self.login, methods=['GET', 'POST'])

    def login(self):
        if request.method == 'GET':
            return render_template('login.html')

        email = request.form['emailForm']
        senha = request.form['senhaForm']

        user = Usuario.query.filter_by(email=email, senha=self.hash(senha)).first()

        if not user:
            return 'nome ou senha incorretos'

        login_user(user)
        return redirect(url_for('paginaprincipal.principal'))