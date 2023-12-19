#     DDL

import random
import sqlalchemy
import os
import sqlalchemy.orm
from dotenv import load_dotenv
from faker import Faker
from geoalchemy2 import Geometry
from .dml import User


load_dotenv()




def main(##paramaetr wywołujący parametr URL z sqlalch
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



### Create, tworzty sesje(połaczenie) z naszą bazą danych z której/do któej będziemy coś przestłać

Session = sqlalchemy.orm.sessionmaker(bind=engine) #tworzymy sesje jako klase(tworzymy jej realizacje)
session = Session()

lista_userow: list =[]


fake = Faker()

fake.name()
for item in range(10_000):
    lista_userow.append(
        User(
            name=fake.name(),
            location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'  # spacja, a nie przecinek
        )
    )

session.add_all(lista_userow)
session.commit()


### Read /Select

users_from_db = session.query(User).all()
for user in users_from_db:
    if user.name == 'Scott Wilkins':
        user.query.filter_by(name='Scott Wilkins')
    print(user.name)


session.commit()


session.flush()
connection.close()
engine.dispose()):


