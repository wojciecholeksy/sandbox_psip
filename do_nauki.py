'''stan_konta = input('Podaj stan konta:') //input-wyświetla tekst
stan_konta = int(stan_konta)// int-rodzaj zmiennej
stan_konta = stan_konta + 500* 2
print(stan_konta) //print Wyświetl '''


'''x = 9
y = x//3
x =x**3
print(y)'''
'''temperature = input('Jaką mamy obecnie temperaturę?')
szczęśliwy = False
temperature = int(temperature)
if temperature > 10 and szczęśliwy: /and obydwa warunki muszą być spełnione
     print('Wyjdź, bo jest ciepło')
elif temperature > -10 or szczęśliwy:  / or jeden warunek wystarczy
     print('Ubierz się ciepło')
else:
    print('Nie wychodź')'''

'''for i in range(1,10,2):
   if i ==5:
      continue
   print(i)'''


'''temperature = 11'''

'''while temperature > 10:
    print('Temperatura jest ok', temperature)
    temperature  -= 1'''


'''oceny = [4,5, 3, 2, 1, 6, 4]'''

'''for i in range(len(oceny)) :
    print(oceny[i], end =' ')

for ocena in oceny:
        print(ocena, end=' ')'''
'''print()'''

'''for i, ocena in enumerate(oceny) :
    if i%2 == 0 and ocena >= 3 :
        print(i, ocena)


for i, ocena in enumerate(oceny):
    oceny[i] += 1

print(oceny)'''

# import module
'''import random as r

ph_no = []

# pierwsza cyfra powinna przyjąć wartość od 0 do 9
ph_no.append(r.randint(0, 9))'''

'''# pętla for służy do dołączenia 8 pozostałych liczb.
# pozostałe 8 cyfr będzie z zakresu  od 0 do 9.
for i in range(0, 9):
    ph_no.append(r.randint(0, 9))

# printing the number
for i in ph_no:
if
    print(i, i, , end="")'''

'''ph_nu = []
ph_nu.append('+(48) ')
for i in range(9):
    if  i == 3 or i ==6:
        ph_nu.append('-')
    ph_nu.append(str(random.randint(0,9)))
print(''.join(ph_nu))
print('Maciej, zadzwoń do mnie, czekam!!!')'''

'''import random as r
ph_nu = []
ph_nu1 = []
ph_nu2 = []
ph_nu3 = []
for i in range(0, 3):
    ph_nu1.append(r.randint(0, 9))
    ph_nu2.append(r.randint(0, 9))
    ph_nu3.append(r.randint(0, 9))

ph_nu1 = ph_nu1 
ph_nu2 = ph_nu2
ph_nu3 = ph_nu3

areacode= 48
/////#///print('+','(',areacode,')', ph_nu1 ,ph_nu2, ' ', ph_nu3)'''


'''import unsers_list
user = random.choice(unsers_list)
ph_nu = []
ph_nu = ['+(48) ']
for i in range(9):
    if i == 3 or i == 6:
        ph_nu.append('-')
    ph_nu.append(str(random.randint(0, 9)))
phone_number = ''.join(ph_nu)

print(f'{user["name"]}, zadzwoń do mnie, mój numer telefonu to: {phone_number}')
'''



'''unsers_name = ["Alice", "Bob", "Charlie", "David"]  # Add the names you want

# Randomly select a name from the list
name = random.choice(unsers_name)'''

'''ph_nu = ['+(48) ']
for i in range(9):
    if i == 3 or i == 6:
        ph_nu.append('-')
    ph_nu.append(str(random.randint(0, 9))
phone_number = ''.join(ph_nu)

print(f'{name}, zadzwoń do mnie, mój numer telefonu to: {phone_number}')'''
"""def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result
"""




'''def invert(lst):
    return [-x for x in lst]


lst = [3,4,6,3,3,4,6]
result = invert(lst)
print(result)'''

'''def count_sheep(n):
    murmur = ''
    for i in range(1, n + 1):
        murmur += f"{i} sheep..."
    return murmur

n = 3
result = count_sheep(n)
print(result'''





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

if __name__ == "__main__":
    czy_pierwsza()


def predokosc_srednia():
t = int(input())
for _ in range(t):

    v1 = int(input())
    v2 = int(input())

    vs = (v1 + v2)//2

    print(int(vs))
predokosc_srednia()


def predokosc_srednia_harmoniczna():     #średnia harmoniczna (mierzona w dwie strony)
    t = int(input())
    for _ in range(t):
        v1, v2 = map(int, input().split())
        vs = (2 * v1 * v2) // (v1 + v2)

        print(int(vs))

if __name__ == "__main__":
    predokosc_srednia_harmoniczna()







