from app import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(70), nullable=False)
    senha = db.Column(db.String(30), nullable=False)

class Simulacao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(30), nullable=False)
    valor_aplicado = db.Column(db.Float, nullable=False)
    cdi = db.Column(db.Float, nullable=False)
    cdi_sobras = db.Column(db.Float, nullable=False)
    dias = db.Column(db.Integer, nullable=False)
    rentabilidade_bruta = db.Column(db.Integer, nullable=False)
    saldo_total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Faixas_lca_pre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor_minimo = db.Column(db.Numeric(10, 2), nullable=False)
    valor_maximo = db.Column(db.Numeric(10, 2), nullable=False)
    taxa = db.Column(db.Numeric(10, 2), nullable=False)
    dias_liquidez = db.Column(db.Integer, nullable=False)
    dias_vencimento = db.Column(db.Integer, nullable=False)