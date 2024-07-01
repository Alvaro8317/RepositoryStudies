import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_lite_file_name = '../database.db'
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f'sqlite:///{os.path.join(base_dir, sql_lite_file_name)}'
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
