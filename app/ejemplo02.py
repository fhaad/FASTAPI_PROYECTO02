import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy .ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connect_info = 'mysql+pymysql://root:Haad91280567#@localhost:3306/marketing?charset=utf8'
engine = create_engine(connect_info)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base

