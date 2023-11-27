def get_map_of(coordinates:list, lista_imion)->None:
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