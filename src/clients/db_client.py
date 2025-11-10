class DBClient:
    def __init__(self, table, db_session):
        self.table = table
        self.db_session = db_session

    def insert_client(self, into_data):
        db_client = self.table(nome=into_data.nome, email=into_data.email)
        self.db_session.add(db_client)

        return db_client
    
    def update_client(self, update_data):
        db_client = self.db_session.query(self.table).filter(self.table.cliente_id == update_data.cliente_id).first()
        
        if db_client is None:
            return None
        
        db_client.nome = update_data.nome
        db_client.email = update_data.email

        self.db_session.commit()
        self.db_session.refresh(db_client)

        return db_client
    

    def delete_client(self, delete_data):
        db_client = self.db_session.query(self.table).filter(self.table.cliente_id == delete_data.cliente_id).first()
        
        if db_client is None:
            return None
        
        self.db_session.delete(db_client)
        self.db_session.commit()

        return db_client
    

    def get_client(self, get_data):
        db_client = self.db_session.query(self.table).filter(self.table.cliente_id == get_data.cliente_id).first()
        
        if db_client is None:
            return None
        
        return db_client


    def get_all_client(self):
        return self.db_session.query(self.table).all()

    
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
