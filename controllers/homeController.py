from flask import Blueprint, render_template

class HomeController:
    def __init__(self):
        self.blueprint = Blueprint('/', __name__)
        self._add_rotas()

    def _add_rotas(self):
        self.blueprint.add_url_rule('/', view_func=self.home)

    def home(self):
        return render_template('home.html')