from db import db
from flask_login import UserMixin
from sqlalchemy import Numeric

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=False, nullable=False)
    sobrenome = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    senha = db.Column(db.String(255), unique=True, nullable=False)

    def get_id(self):
        return str(self.id_usuario)

class Vaga(db.Model):
    __tablename__ = 'vagas'

    id_vaga = db.Column(db.Integer, primary_key=True)
    id_local = db.Column(db.Integer, db.ForeignKey('localizacao.id_local'))

class Localizacao(db.Model):
    __tablename__ = 'localizacao'

    id_local = db.Column(db.Integer, primary_key=True)
    nome_rua = db.Column(db.String(35), unique=False, nullable=False)
    latitude = db.Column(Numeric(9, 6), unique=False, nullable=False)
    longitude = db.Column(Numeric(9, 6), unique=False, nullable=False)

class Consulta(db.Model):
    __tablename__ = 'consulta'

    id_consulta = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    data = db.Column(db.DateTime, unique=False, nullable=False)
    hora = db.Column(db.Time, unique=False, nullable=False)


class Previsao(db.Model):
    __tablename__ = 'previsao'

    id_previsao = db.Column(db.Integer, primary_key=True)
    id_vaga = db.Column(db.Integer, db.ForeignKey('vagas.id_vaga'))
    data = db.Column(db.DateTime, unique=False, nullable=False)
    hora = db.Column(db.Time, unique=False, nullable=False)
