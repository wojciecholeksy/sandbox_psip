def liczby_pierwsze(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def czy_pierwsza():
    t = int(input())            #podaj ilość testów
    for _ in range(t):
        n = int(input())        #podaj wartości liczbowe
        if liczby_pierwsze(n):
            print("Tak")
        else:
            print("Nie")


# czy_pierwsza()


def predokosc_srednia():
    t = int(input())
    for _ in range(t):

        v1 = int(input())
        v2 = int(input())
        vs = (v1 + v2)//2

        print(int(vs))
# predokosc_srednia()


def predokosc_srednia_harmoniczna():     #średnia harmoniczna (mierzona w dwie strony)
    t = int(input())
    for _ in range(t):
        v1, v2 = map(int, input().split())
        vs = (2 * v1 * v2) // (v1 + v2)

        print(int(vs))

# predokosc_srednia_harmoniczna()


def zadanie_probne():
    a = int(input())
    b = int(input())
    # if a <=200 and b <=200:
    print(a+b)



# zadanie_probne()
def zad_probne()->int:
    A = int(input())
    B = int(input())
    print(A+B)
zadanie_probne()