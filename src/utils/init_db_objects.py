from sessions.postgresql_session import PostgreSQLSession
from sqlalchemy.exc import IntegrityError


POSTGRESQL_DB_SESSION = PostgreSQLSession()
BASE = POSTGRESQL_DB_SESSION.get_base()


def db_session():
    db_session = POSTGRESQL_DB_SESSION.session_factory()
    
    try:
        yield db_session

    except Exception as e:
        db_session.rollback()
        raise e
    
    finally:
        db_session.close()
