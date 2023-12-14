


############################################################
def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('podaj nowe imię: ')
            user['nick'] = input('podaj nową ksywę: ')
            user['posts'] = int(input('podaj liczbę postów: '))


def add_user_to(users_list: list) -> None:  # .list informacja o tym że to bedzize lista       None - że nie zwróci nic
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    city = input('Podaj miasto')
    name = input('Podaj imię')
    nick = input('Podaj nick')
    posts = input('Podaj liczbę postów')
    users_list.append({'name': name, 'nick': nick, 'posts': posts, "city": city})


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - users list
    :return: None
    """
    tmp_list = []
    name = input('Podaj imię użytkownika do usunięcia: ')
    for user in users_list:
        if user["name"] == name:  # musi być nawias kwadratowy ponieważ odwołujemy się do listy
            tmp_list.append(user)
            # users_list.remove(user)
    print(f'Znaleziono użytkowników: ')
    print('0: Usuń wszystkich ')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(
        f'Wybierz użytkownika do usunięcia: '))  # wynikiem operacji inpunt jest string więc musimy zMIENIĆ go dalej na ineger
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

    # users_list.remove(tmp_list[numer-1])


def show_users_from(users_list: list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')


from bs4 import BeautifulSoup
import requests
import folium
from dane import users_list

#import re

# pobranie strony
#nazwa_miejscowości = ['Gdańsk']

###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^MAPA^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def get_coordinates_of(city: str) -> [float, float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'   #pobieranie strony internetowej

    response = (requests.get(url=adres_URL))
    response_html = BeautifulSoup(response.text, 'html.parser')

    response_html_latitude = response_html.select('.latitude')[1].text  # . (kropka) ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',','.'))  # wynikiem jest string, a my chcemy liczbę dlatego zamieniamy przecinki na kropki i konwertujemy na float
    response_html_longitude = response_html.select('.longitude')[1].text  # . (kropka) ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]


# for item in nazwa_miejscowości:
#     print(get_coordinates_of(item))
# Rysowanie mapy



def get_map_one_user(user: str) -> None:
    city = get_coordinates_of(user["city"])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=14)

    folium.Marker(
        location=city,
        popup=f'Tu rządzi: {user["name"]} z GEOINFORMATYKI 2023 \n OU YEAHHHH'
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')



def get_map_of(users: list[dict,dict]) -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=7)
    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]} \n'                  
                  f'Liczba postów {user["posts"]}'
        ).add_to(map)
        map.save('mapka.html')


from dane import users_list




def gui(users_list) -> None:
    while True:
        print(f'MENU: \n'
              f'0. Zakończ program\n'
              f'1. Wyświetl uzytkowników\n'
              f'2. Dodaj użytkownika\n'
              f'3. Aktualizuj użytkownika\n'
              f'4. Usuń użytkownika\n'
              f'5. Modyfikuj użytkownika\n'
              f'6. Dodaj mapkę z jednym użytkownikiem\n'
              f'7. Dodaj mapkę ze wszystkimi użytkownikami\n'
              )
        menu_opction = input('Podaj funkcję do wywołania ')
        print(f'wybrano funkcję{menu_opction}')

        match menu_opction:
            case '0':
                print('Kończę pracę ')
                break
            case '1':
                print('Wyświetlanie listy użytkowników')
                show_users_from(users_list)
            case '2':
                print('Dodaję użytkownika ')
                add_user_to(users_list)
            case '3':
                print('Aktualizuj użytkownika')
                update_user(users_list)
            case '4':
                print('Usuń użytkownika')
                remove_user_from(users_list)
            case '5':
                print('Modyfikuję użytkownika')
                update_user(users_list)
            case '6':
                print('Rysuję mapę z użytkownikiem')
                user = input('Podaj nazwę użytkownika do modyfikacji:')
                for item in users_list:
                    if item['name'] == user:
                        get_map_one_user(item)
            case '7':
                print('Rysuję mapę ze wszystkimi użytkownikami')
                get_map_of(users_list)


def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
    print(nick_of_user)
    for user in users_list:
        if user["nick"] == nick_of_user:
            print("Znaleziono !!!")
            user['name'] = input("Podaj nowe imię: ")
            user['nick'] = input("Podaj nowA ksywkę: ")
            user['posts'] = int(input("Podaj liczbę postów: "))
            user['city'] = input('Podaj miasto')
