###Beatifulsoap
import bs4 from Beautisoap


def get_coordinates_of(city: str) -> [float, float]:
    # Tworzy adres URL do strony Wikipedii dotyczącej podanego miasta
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    # Wysyła zapytanie HTTP GET do strony Wikipedii
    response = rq.get(url=adres_URL)

    # Parsuje treść strony HTML przy użyciu biblioteki BeautifulSoup
    response_html = BeautifulSoup(response.text, 'html.parser')

    # Wybiera elementy o klasie 'latitude' i 'longitude' z treści strony
    response_html_latitude = response_html.select('.latitude')[1].text
    response_html_longitude = response_html.select('.longitude')[1].text

    # Zamienia przecinki na kropki i konwertuje na float
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    # Zwraca listę zawierającą współrzędne geograficzne [szerokość, długość]
    return [response_html_latitude, response_html_longitude]
