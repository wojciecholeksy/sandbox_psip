from dane import users_list

def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('podaj nick uzytkownika do modyfikacji')
    print(nick_of_user)
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('Znaleziono !!!')
            user['name'] = input('podaj nowe imię: ')
            user['nick'] = input('podaj nową ksywę: ')
            user['posts'] = int(input('podaj liczbę postów: '))


update_user(users_list)
for user in users_list:
    print(user)