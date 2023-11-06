def show_unsers_from(users_list: list)->None:

from dane import users_list
from utils.my_function import add_user_to, remove_user_from, show_users_from
def gui()-> None:
    while True:
        print(f'Witaj użytkowniku \n'
            f'1: Wyświetl użytkowników: \n'
            f'2: Dodaj użytkownika: \n'
            f'3: Usuń użytkownika: \n'
            f'4: Modyfikuj użytkownika: \n'
                 )

        menu_option = input('Podaj funkcję do wywołania: ')
        print(f'Wybrano funkcje {menu_option}')

        match menu_option:
            case'0':
                print('Kończę pracę.')
                break
            case '1':
                print("Wyświetlam listę użytkowników")
                show_users_from(users_list)
            case '2':
                print("Dodaję użytkownika")
                add_user_to(users_list)
            case '3':
                print('Usuwanie użytkownika')
                remove_user_from(users_list)
            case '4':
                print("Modyfikuj użytkownika:")
                print('to będzie zrobione niedługo')

    gui()
