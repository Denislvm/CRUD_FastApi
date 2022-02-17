from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "postgresql://user:password@postgresserver/db"
DATABASE_URL = "postgresql://fastapi_user:pass@localhost:5432/fastapi_db"

engine = create_engine(
    DATABASE_URL
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()