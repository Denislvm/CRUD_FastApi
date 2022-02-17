import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tables(Base):
    __tablename__ = "tables"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, unique=True)
    email = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    date = sa.Column(sa.Date)

