from flask import Blueprint, render_template
from flask_login import login_required

class PrincipalController:
    def __init__(self):
        self.blueprint = Blueprint('paginaprincipal', __name__)
        self._add_rotas()

    def _add_rotas(self):
        self.blueprint.add_url_rule('/', view_func=self.principal, methods=['GET', 'POST'])

    @login_required
    def principal(self):
        return render_template('paginaprincipal.html')