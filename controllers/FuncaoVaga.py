from datetime import datetime


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


# EXEMPLO DE USO

historico_exemplo = [
    {
        "status": "LIVRE",
        "data_hora": datetime(2026, 5, 20, 8, 0)
    },
    {
        "status": "OCUPADA",
        "data_hora": datetime(2026, 5, 20, 9, 0)
    },
    {
        "status": "LIVRE",
        "data_hora": datetime(2026, 5, 27, 8, 30)
    }
]

resultado = calcular_probabilidade_vaga(
    vaga_id=1,
    data_consulta=datetime.now(),
    historico=historico_exemplo
)

print(resultado)
