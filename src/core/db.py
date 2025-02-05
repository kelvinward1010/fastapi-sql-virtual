from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
