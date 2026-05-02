from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = create_engine("postgresql://postgres:admin@localhost:5432/clickerdb")
Session = sessionmaker(bind=DB_URL,autoflush=False,autocommit=False)

Base = declarative_base()


