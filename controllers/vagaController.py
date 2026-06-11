from datetime import datetime
from models import HistoricoOcupacao, Vaga
from math import sqrt


def vagas_proximas(lat, lon, raio=0.005):

    vagas = Vaga.query.all()

    resultado = []

    for vaga in vagas:

        distancia = sqrt(
            (vaga.latitude - lat) ** 2 +
            (vaga.longitude - lon) ** 2
        )

        if distancia <= raio:

            resultado.append(vaga)

    return resultado

def obter_historico(vaga_id):

    registros = HistoricoOcupacao.query.filter_by(
        vaga_id=vaga_id
    ).all()

    historico = []

    for registro in registros:

        historico.append({
            "status": registro.status,
            "data_hora": registro.data_hora
        })

    return historico


def calcular_probabilidade_vaga(vaga_id, data_consulta, historico):

    """
    vaga_id = ID da vaga
    data_consulta = data/hora atual
    historico = lista de registros vindos do banco

    Exemplo do historico:
    [
        {
            "status": "LIVRE",
            "data_hora": datetime(2026, 5, 20, 8, 0)
        },
        {
            "status": "OCUPADA",
            "data_hora": datetime(2026, 5, 20, 9, 0)
        }
    ]
    """

    hora = data_consulta.hour
    dia_semana = data_consulta.weekday()

    total_registros = 0
    vagas_livres = 0

    for registro in historico:

        data_registro = registro["data_hora"]

        if data_registro.weekday() == dia_semana:

            if abs(data_registro.hour - hora) <= 1:

                total_registros += 1

                if registro["status"] == "LIVRE":
                    vagas_livres += 1

    if total_registros == 0:
        probabilidade = 50
    else:
        probabilidade = int((vagas_livres / total_registros) * 100)

    status_previsto = "LIVRE" if probabilidade >= 50 else "OCUPADA"

    return {
        "vaga_id": vaga_id,
        "probabilidade_livre": probabilidade,
        "status_previsto": status_previsto,
        "analisados": total_registros
    }
