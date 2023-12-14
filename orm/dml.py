#   DML
import random

import sqlalchemy
import os
import sqlalchemy.orm
from dotenv import load_dotenv
from faker import Faker
from geoalchemy2 import Geometry

load_dotenv()


##paramaetr wywołujący parametr URL z sqlalch
db_params = sqlalchemy.URL.create(
    drivername= 'postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    port=os.getenv("POSTGRES_PORT")
)

engine = sqlalchemy.create_engine(db_params)

#definiujemy połączenie do silnika
connection = engine.connect()

Base= sqlalchemy.orm.declarative_base()


## trzeba pamientać o dodaniu extention
class User(Base):
    __tablename__ = "mm_table"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True) #dla bazy danych intiger automatyczie taje typ serial (autonumerowanie)
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location = sqlalchemy.Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)



Base.metadata.create_all(engine)

connection.close()
engine.dispose()
