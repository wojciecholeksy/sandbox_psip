
from dane import users_list
#dodaj użytkownika do/list- funkcja dostaje liste/ (none) oznacza, że funkcja nie oddaje nic
# def add_user_to(users_list: list) -> None:
#
#     add object to llist
#     :param users_list: list - user list
#     :return: None'''

#     name = input('Podaj imię ?:')
#     posts = input('Podaj liczbę postów ?:')
#     users_list.append({'name': name, 'posts': posts})'''
# #add_user_to(users_list)
# #users_list.remove({"name":"Agata", "nick":"Ajgaciu", "posts":1600})
#
# '''for user in users_list:
#     name = input('Podaj imię użytkownika do usunięcia:')
#         if user['name'] == name:
#              print(f'Znaleziono użytkownika {user} ')
# users_list.remove(user)


'''def remove_user_from(users_list: list) -> None:

    tmp_list = []
    name = input('Podaj imię użytkownika do usunięcia : ')
    for user in users_list:
        if user['name'] == name:
            tmp_list.append(user)
    print(f'Znaleziono użytkownika:  ')
    print('0: Usuń wszystkich znalezionych użytkowników: ')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek}: {user_to_be_removed}')
    numer =int(input(f'Wybierz numer użytkownika do usunięcia: '))
    if (numer) == 0:
        for user in users_list:
            if user['name'] == name:
                users_list.remove(user)
        else:
            users_list.remove(tmp_list[numer-1])'''

#for user in users_list:
   # print(f'Twój znajomy {user ["name"]} dodał {user ["posts"]} postów. ')
   # print(f" Czas odejść od komputera i wyjść z domu !!!")



''' pseudokod pętli w pythonie instrukcja: for item in nazwa_listy:
print(f'Twój znajomy {zmienna_na_dane[0]["nick"]} opublikował  {zmienna_na_dane[0]["posts"]} postów!!!')
'''


from dane import users_list

def add_user_to(users_list:list) -> None:        #    .list informacja o tym że to bedzize lista       None - że nie zwróci nic
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """

    name=input('Podaj imię')
    nick=input('Podaj nick')
    posts=input('Podaj liczbę postów')
    users_list.append({'name':name,'nick':nick, 'posts': posts})
#add_user_to(users_list)
def remove_user_from(users_list:list) -> None:
    """
    remove object from list
    :param users_list: list - users list
    :return: None
    """
    tmp_list=[]
    name=input('Podaj imię użytkownika do usunięcia: ')
    for user in users_list:
        if user["name"]==name:                                 #musi być nawias kwadratowy ponieważ odwołujemy się do listy
            tmp_list.append(user)
            #users_list.remove(user)
    print(f'Znaleziono użytkowników: ')
    print('0: Usuń wszystkich ')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    numer=int(input(f'Wybierz użytkownika do usunięcia: ')) #wynikiem operacji inpunt jest string więc musimy zMIENIĆ go dalej na ineger
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])

    #users_list.remove(tmp_list[numer-1])
remove_user_from(users_list)


#print(f'Twój znajomy {zmienna_na_dane[0]["nick"]} opublikował {zmienna_na_dane[0]["posts"]} postów!!!')         #    te f (f-string) przed ''klauzula w python do zmiennych jaką wstawiamy     []do którego elementu listy się odwołujemy

for user in users_list:
    print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')