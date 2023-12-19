import psycopg2 as ps
import requests as rq
from bs4 import BeautifulSoup
import folium


############################################################

db_pharams = ps.connect(
    database= 'postgres',
    user= "postgres",
    password= "psip2023",
    host= "localhost",
    port= 5432
)

cursor = db_pharams.cursor()


def add_user_to() -> None:  # .list informacja o tym że to bedzize lista       None - że nie zwróci nic
    city = input('Podaj miasto').strip()
    name = input('Podaj imię').strip()
    nick = input('Podaj nick').strip()
    posts = input('Podaj liczbę postów').strip()

    sql_query_1 = f"INSERT INTO public.my_geotinder(city, name, nick, posts)VALUES ('{city}','{name}', '{nick}','{posts}');"
    cursor.execute(sql_query_1)
    db_pharams.commit()

#
def update_user() -> None:
    nick_of_user = input('Podaj nick uzytkownika do modyfikacji')
    sql_query_1 = f" SELECT * FROM public.my_geotinder WHERE nick =  '{nick_of_user}';"
    cursor.execute(sql_query_1)
    print('Znaleziono !!!')
    city = input('Podaj nazwę nowego miasta: ').strip()
    name = input('Podaj nowe imię: ').strip()
    nick = input('Podaj nowy nick: ').strip()
    posts = int(input('Podaj liczbę postów: ')).strip()
    sql_query_2 = f"UPDATE public.my_geotinder SET city ='{city}',name ='{name}', nick ='{nick}',posts = '{posts}' WHERE nick = '{nick_of_user}';"
    cursor.execute(sql_query_2)
    db_pharams.commit()




def remove_user_from() -> None:
    name = input('Podaj imię geoinformatyka, któru już nie jest samotny, aby usunąć go z listy przegrywów: ')
    sql_query_1 = f" SELECT * FROM public.my_geotinder WHERE name='{name}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    print(f'Znaleziono użytkowników: ')
    print('0: Usuń wszystkich ')

    for numerek, user_to_be_removed in enumerate(query_result):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz użytkownika do usunięcia: '))  # wynikiem operacji inpunt jest string więc musimy zMIENIĆ go dalej na ineger
    if numer == 0:
        sql_query_2 = f"DELETE FROM public.my_geotinder: "
        cursor.execute(sql_query_2)
        db_pharams.commit()
    else:
        sql_query_2 = f"DELETE FROM public.my_geotinder WHERE name='{query_result[numer-1][2]}';"
        cursor.execute(sql_query_2)
        db_pharams.commit()



    # for user in users_list:
    #     if user["name"] == name:  # musi być nawias kwadratowy ponieważ odwołujemy się do listy
    #         tmp_list.append(user)
    # users_list.remove(user)
    # users_list.remove(tmp_list[numer-1])


def show_users_from() -> None:
    sql_query_1 = f' SELECT * FROM public.my_geotinder'
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for row in query_result:
        print(f'Twój znajomy {row[2]} opublikował {row[4]} postów')




#import

# pobranie strony
#nazwa_miejscowości = ['Gdańsk']


def get_coordinates_of(city: str) -> [float, float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'   #pobieranie strony internetowej

    response = (rq.get(url=adres_URL))
    response_html = BeautifulSoup(response.text, 'html.parser')

    response_html_latitude = response_html.select('.latitude')[1].text  # . (kropka) ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',','.'))  # wynikiem jest string, a my chcemy liczbę dlatego zamieniamy przecinki na kropki i konwertujemy na float
    response_html_longitude = response_html.select('.longitude')[1].text  # . (kropka) ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


# for item in nazwa_miejscowości:
#     print(get_coordinates_of(item))
# Rysowanie mapy



def get_map_one_user() -> None:
    city = input('Podaj miasto użytkownika: ')
    sql_query_1 = f" SELECT * FROM public.my_geotinder WHERE city ='{city}';"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    city = get_coordinates_of(city)
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14)
    for user in query_result:
        folium.Marker(location=city,
        popup=f'Użytkownik: {user[2]} \n'
        f' Liczba postów: {user[4]}'
        ).add_to(map)
    map.save(f'mapka_{query_result[0][1]}.html')


def get_map_of() -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=7)
    sql_query_1 = f" SELECT * FROM public.my_geotinder;"
    cursor.execute(sql_query_1)
    query_result = cursor.fetchall()
    for user in query_result:
        folium.Marker(
            location=get_coordinates_of(city=user[1]),
            popup=f'Użytkownik: {user[2]} \n'                  
            f'Liczba postów {user[4]}'
            ).add_to(map)
        map.save('mapka.html')


from dane import users_list




def gui() -> None:
    while True:
        print(f'MENU: \n'
              f'0. Zakończ program\n'
              f'1. Wyświetl samotnych geoinformatyków z Twojej okolicy\n'
              f'2. Dodaj użytkownika\n'
              f'3. Usuń użytkownika\n'
              f'4. Modyfikuj użytkownika\n'
              f'5. Dodaj mapkę z jednym samotnym geoinformatykiem\n'
              f'6. Dodaj mapkę ze wszystkimi samotnymi geoinformatykami\n'
              )
        menu_opction = input('Podaj funkcję do wywołania ')
        print(f'wybrano funkcję{menu_opction}')

        match menu_opction:
            case '0':
                print('Kończę pracę ')
                break
            case '1':
                print('Wyświetlanie listy użytkowników')
                show_users_from()
            case '2':
                print('Dodaję użytkownika ')
                add_user_to()
            case '3':
                print('Usuń użytkownika')
                remove_user_from()
            case '4':
                print('Modyfikuję użytkownika')
                update_user()
            case '5':
                print('Rysuję mapę z użytkownikiem')
                get_map_one_user()
            case '6':
                print('Rysuję mapę ze wszystkimi użytkownikami')
                get_map_of()





# class User:
#     def __init__(self, city, name, nick, posts):   #init oznacza rozpoczęcie, funkcja definiuje jakie parametry musi posiadać postać z klasy
#         self.city = city
#         self.name = name
#         self.nick = nick
#         self.posts = posts
# def pogoda_z(miasto:str): #definiujemy funkcje do której dodajemy nazwe miata (typ danych string)
#     url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"  #zmienna z linkiem, a w nawiasie dzięki f"" dodajemy wartość zmiennej miasto
#     return rq.get(url).json() # od razu zwracamy to co funkcja wywołuje, bez zajmowania miejsca w pamięci
#
# npc_1 = User(city="Stężyca_(województwo_lubelskie)", name="Wojciech", nick="Panwowo", posts= 1)     #linijki służące do tworzenia obiektów
# npc_2 = User(city="Lublin", name="Andrzej", nick="Endrju", posts= 60)         #od teraz powstaje npc z Lublina i "buum" już jest
# print(npc_1.city)   #(nazwa klasy.wywoływany parametr)
# print(npc_2.city)
#
# print(npc_1.pogoda_z(npc_1.city))
# print(npc_2.pogoda_z(npc_2.city))
