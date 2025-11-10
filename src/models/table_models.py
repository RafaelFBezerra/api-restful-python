import sqlalchemy as sa

from utils.init_db_objects import BASE


class ClientTable(BASE):
    __tablename__ = "clientes"

    cliente_id = sa.Column(sa.Integer, primary_key=True, index=True)
    nome = sa.Column(sa.String, index=True, nullable=False)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)


class ProductTable(BASE):
    __tablename__ = "produtos_favoritos"

    cliente_id = sa.Column(sa.Integer, primary_key=True, index=True)
    id_produto = sa.Column(sa.String, primary_key=True, index=True)
    titulo = sa.Column(sa.String, index=True, nullable=False)
    imagem = sa.Column(sa.String, index=True, nullable=False)
    preco = sa.Column(sa.String, index=True, nullable=False)
    review = sa.Column(sa.String, index=True, nullable=True)
