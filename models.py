from database import db
from datetime import datetime


class ControleAcesso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colaborador_liberado = db.Column(db.Boolean, default=False)


class Colaborador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    setor = db.Column(db.String(80), nullable=False)
    cargo = db.Column(db.String(80), nullable=False)
    ativo = db.Column(db.Boolean, default=True)


class EPI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(30), unique=True, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    unidade = db.Column(db.String(20), nullable=False)
    ativo = db.Column(db.Boolean, default=True)


class PedidoEPI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now)

    matricula = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(120), nullable=False)

    tipo_item = db.Column(db.String(80), nullable=False)
    descricao_item = db.Column(db.String(200), nullable=False)
    tamanho = db.Column(db.String(50), nullable=False)

    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(30), default="Solicitado")


class PedidoAlmoxarifado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now)
    matricula = db.Column(db.String(20), nullable=False)
    solicitante = db.Column(db.String(120), nullable=False)
    setor = db.Column(db.String(80), nullable=False)
    item = db.Column(db.String(200), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.Text)
    status = db.Column(db.String(30), default="Solicitado")
