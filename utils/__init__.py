import psycopg2 as ps
import requests as rq
from bs4 import BeautifulSoup
import folium


# def pogoda_z(self: str):  # definiujemy funkcje do której dodajemy nazwe miata (typ danych string)
#     url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"  # zmienna z linkiem, a w nawiasie dzięki f"" dodajemy wartość zmiennej miasto
#     return rq.get(url).json()


# class User:
#     def __init__(self, city, name, nick, posts):   #init oznacza rozpoczęcie, funkcja definiuje jakie parametry musi posiadać postać z klasy
#         self.city = city
#         self.name = name
#         self.nick = nick
#         self.posts = posts
#     def pogoda_z(self,miasto: str): #definiujemy funkcje do której dodajemy nazwe miata (typ danych string)
#         url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"  #zmienna z linkiem, a w nawiasie dzięki f"" dodajemy wartość zmiennej miasto
#         return rq.get(url).json() # od razu zwracamy to co funkcja wywołuje, bez zajmowania miejsca w pamięci
#
# npc_1 = User(city="warszawa", name="Wiktoria", nick="Wiki", posts= 123)     #linijki służące do tworzenia obiektów
# npc_2 = User(city="lublin", name="Andrzej", nick="Endrju", posts= 60)         #od teraz powstaje npc z Lublina i "buum" już jest
# print(npc_1.city)   #(nazwa klasy.wywoływany parametr)
# print(npc_2.city)
#
# print(npc_1.pogoda_z(npc_1.city))
# print(npc_2.pogoda_z(npc_2.city))