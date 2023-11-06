from dane import users_list

#dodaj użytkownika do/list- funkcja dostaje liste/ (none) oznacza, że funkcja nie oddaje nic
def add_user_to(users_list: list) -> None:
    """
    add object to llist
    :param users_list: list - user list
    :return: None
    """
    name = input('Podaj imię ?:')
    posts = input('Podaj liczbę postów ?:')
    users_list.append({'name': name, 'posts': posts})

add_user_to(users_list)

for user in users_list:
    print(f'Twój znajomy {user ["name"]} dodał {user ["posts"]} postów ')
   # print(f" Czas odejść od komputera i wyjść z domu !!!")



''' pseudokod pętli w pythonie instrukcja: for item in nazwa_listy:
print(f'Twój znajomy {zmienna_na_dane[0]["nick"]} opublikował  {zmienna_na_dane[0]["posts"]} postów!!!')
'''