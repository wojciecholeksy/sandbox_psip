import psycopg2 as ps
from dane import users_list

db_pharams = ps.connect(
    database= 'postgres',
    user= "postgres",
    password= "psip2023",
    host= "localhost",
    port= 5432
)

cursor = db_pharams.cursor()

# engine = sqlalchemy.create_engine(db_pharam)
# connection = engine.connect()

def import_user(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1 = f"INSERT INTO public.my_geotinder(city, name, nick, posts)VALUES ('{nick['city']}', '{nick['name']}','{nick['nick']}','{nick['posts']}');"
            cursor.execute(sql_query_1)
            db_pharams.commit()

import_user(input("Dodaj użytkownika o nicku: "))


# def usun_uzytkownika(user:str):
#     sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name='{user}';")
#     connection.execute(sql_query_1)
#     connection.commit()
# cwok = 'stasiu'
# usun_uzytkownika(cwok)
#
#
# def aktualizuj_uzytkownika(user_1:str,user_2:str):
#     sql_query_1 =sqlalchemy.text(f"UPDATE public.my_table SET name='{user_1}' WHERE name = '{user_2}';")
#     connection.execute(sql_query_1)
#     connection.commit()
# aktualizuj_uzytkownika(
#     user_1=input('Na kogo zamienić?'),
#     user_2=input('Kogo zamienić?')
# )