class DBProductTable:
    def __init__(self, table, db_session):
        self.table = table
        self.db_session = db_session

    def insert_favorite_products(self, into_data):
        db_client = self.table(
            cliente_id=into_data.cliente_id,
            id_produto=into_data.id_produto,
            titulo=into_data.titulo,
            imagem=into_data.imagem,
            preco=into_data.preco,
            review=into_data.review
        )
        self.db_session.add(db_client)

        return db_client


    def get_favorite_products_by_id(self, get_data):
        db_client = self.db_session.query(self.table).filter(self.table.cliente_id == get_data.cliente_id).all()

        if db_client is None:
            return None

        return db_client