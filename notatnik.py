###Beautifulsoap4

from bs4 import BeautifulSoup
import requests
import re
# pobranie strony
nazwa_miejscowości = 'Gdańsk'
def get_coordinates_of(nazwa_miejscowości:str)->[float,float]:

    adres_URL = f'https://pl.wikipedia.org/wiki/{nazwa_miejscowości}'

    response = (requests.get(url=adres_URL))
    response_html = BeautifulSoup(response.text, 'html.parser')

    response_html_latitude = response_html.select('.latitude')[1].text  # . (kropka) ponieważ class
    response_html_latitude = float(response_html_latitude.replace(',','.'))      #wynikiem jest string, a my chcemy liczbę dlatego zamieniamy przecinki na kropki i konwertujemy na float
    response_html_longitude = response_html.select('.longitude')[1].text  # . (kropka) ponieważ class
    response_html_longitude = float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]

for item in nazwa_miejscowości:
    print(response_html_latitude , response_html_longitude)


