import datetime
from app import db, ma

class Contatos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nome = db.Column(db.String(60), nullable=False)
    canal = db.Column(db.String(60), nullable=False)
    valor = db.Column(db.String(60), nullable=False)
    obs = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, nome, canal, valor, obs):
        self.username = username
        self.password = password
        self.nome = nome
        self.canal = canal
        self.valor = valor
        self.obs = obs


class ContatosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'nome', 'canal', 'valor', 'obs', 'created_on')

contato_schema = ContatosSchema()
contatos_schema = ContatosSchema(strict=True, many=True)
