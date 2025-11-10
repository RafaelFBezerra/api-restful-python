from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from utils.constants import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


class PostgreSQLSession:
    def __init__(self):
        self.base = None
        self.engine = None
        self.local_session = None
        self.url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    def get_engine(self):
        if self.engine is None:
            self.engine = create_engine(self.url)
        
        return self.engine

    def get_session(self) -> sessionmaker:
        self.local_session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
    

    def get_base(self) -> declarative_base:
        if self.base is None:
            self.base = declarative_base()

        return self.base
    
    def session_factory(self):
        if self.local_session is None:
            self.get_engine()
            self.get_session()

        return self.local_session()

    def close_session(self):
        if self.local_session is not None:
            self.local_session.close()
