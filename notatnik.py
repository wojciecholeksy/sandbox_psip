###Beautifulsoap4

from bs4 import BeautifulSoup
import requests
import folium
import re
# pobranie strony
nazwa_miejscowości = ['Gdańsk']
def get_coordinates_of(city:str)->[float,float]:

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = (requests.get(url=adres_URL))
    response_html = BeautifulSoup(response.text, 'html.parser')

    response_html_latitude = response_html.select('.latitude')[1].text  # . (kropka) ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',','.'))      #wynikiem jest string, a my chcemy liczbę dlatego zamieniamy przecinki na kropki i konwertujemy na float
    response_html_longitude = response_html.select('.longitude')[1].text  # . (kropka) ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return[response_html_latitude, response_html_longitude]

# for item in nazwa_miejscowości:
#     print(get_coordinates_of(item))
#Rysowanie mapy
user = {"city":'Mińsk_Mazowiecki',"name":"Monika", "nick":"Monia", "posts":1_000_000}

def get_map_one_user(user:str)->None:
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
get_map_one_user(user)



def get_map_of(users:list)->None:
    map = folium.Map(
        location=[52.3, 21.0],
        titles="OpenStreetMap",
        zoom_start=7,

    )
    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user["city"]),
            popup=f'Użytkownik:{user["name"]} \n'
                  f'Liczba postów {user["posts"]}'

        ).add_to(map)
    map.save('mapka.html')
from dane import users_list

get_map_of(users_list)