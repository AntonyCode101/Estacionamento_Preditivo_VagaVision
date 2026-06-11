from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required
from controllers.vagaController import vagas_proximas, obter_historico, calcular_probabilidade_vaga
from datetime import datetime

class PrincipalController:
    def __init__(self):
        self.blueprint = Blueprint('paginaprincipal', __name__)
        self._add_rotas()

    def _add_rotas(self):
        self.blueprint.add_url_rule('/', view_func=self.principal, methods=['GET', 'POST'])

    @login_required
    def principal(self):
        return render_template('paginaprincipal.html')

    def buscar(self):
        dados = request.get_json()

        latitude = dados["latitude"]
        longitude = dados["longitude"]

        vagas = vagas_proximas(
            latitude,
            longitude
        )

        retorno = []

        for vaga in vagas:
            historico = obter_historico(
                vaga.id
            )

            previsao = calcular_probabilidade_vaga(
                vaga.id,
                datetime.now(),
                historico
            )

            retorno.append({
                "id": vaga.id,
                "latitude": vaga.latitude,
                "longitude": vaga.longitude,
                "probabilidade":
                    previsao["probabilidade_livre"],
                "status":
                    previsao["status_previsto"]
            })

        return jsonify(retorno)