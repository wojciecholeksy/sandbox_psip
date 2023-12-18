
import requests #import biblioteki zapytań
from bs4 import BeautifulSoup
import requests
import folium
from dane import users_list
class User:  #tworzymy klase User (nazwy klas piszemy z wielkiej litery
    def __init__(self, miasto):  #self oznacza,
        self.miasto = miasto

    def pogoda_z(self, miasto: str):  # definiujemy funkcje do której dodajemy nazwe miata (typ danych string)/ self powoduje, że muszę mówić npc na początku 16 i 17 linijki przy print
        url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"  # zmienna z linkiem, a w nawiasie dzięki f"" dodajemy wartość zmiennej miasto
        return requests.get(url).json()  # od razu zwracamy to co funkcja wywołuje, bez zajmowania miejsca w pamięci

npc_1 = User(miasto="warszawa")     #linijki służące do tworzenia obiektów
npc_2 = User(miasto="zamosc")         #od teraz powstaje npc z zamościa i "buum" już jest
print(npc_1.miasto)   #(nazwa klasy.wywoływany parametr)
print(npc_2.miasto)

print(npc_1.pogoda_z(npc_1.miasto))
print(npc_2.pogoda_z(npc_2.miasto))

pogoda_z("warszawa")

