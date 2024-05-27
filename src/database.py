from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

sync_engine = create_engine(settings.DATABASE_URL_sqlite, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

def session_factory():
    return SessionLocal()