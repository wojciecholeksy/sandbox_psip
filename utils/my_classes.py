import sqlalchemy

db_pharam = sqlalchemy.URL.create(
    drivername="postgresql+psycopg2",
    username= "postgres",
    password= "psip2023",
    host= "localhost",
    database= "postgres",
    port= 5432
)



engine = sqlalchemy.create_engine(db_pharam)
connection = engine.connect()

def dodaj_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"INSERT INTO public.my_table(name)VALUES ('{user}');")
    connection.execute(sql_query_1)
    connection.commit()
cwok = 'stasiu'
dodaj_uzytkownika(cwok)

def usun_uzytkownika(user:str):
    sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name='{user}';")
    connection.execute(sql_query_1)
    connection.commit()
cwok = 'stasiu'
usun_uzytkownika(cwok)


def aktualizuj_uzytkownika(user_1:str,user_2:str):
    sql_query_1 =sqlalchemy.text(f"UPDATE public.my_table SET name='{user_1}' WHERE name = '{user_2}';")
    connection.execute(sql_query_1)
    connection.commit()
aktualizuj_uzytkownika(
    user_1=input('Na kogo zamienić?'),
    user_2=input('Kogo zamienić?')
)