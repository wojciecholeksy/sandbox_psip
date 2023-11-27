###Beautifulsoap4

from bs4 import BeautifulSoup
import requests
import folium
import re
# pobranie strony
nazwa_miejscowości = ['Gdańsk','Mały_Płock']
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
city = get_coordinates_of(city='Zamość')
map = folium.Map(
    location=get_coordinates_of(city='Zamość'),
    tiles="OpenStreetMap",
    zoom_start=14)

for item in nazwa_miejscowości:
    folium.Marker(
        location=city,
        popup='GEOINFORMATYKA RZĄDZI OU YEEEEAAAH'
    ).add_to(map)
    map.save('mapka.html')