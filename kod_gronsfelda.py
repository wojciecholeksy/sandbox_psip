def szyfruj_gronsfeld(tekst, klucz):
    szyfrogram = ""
    for i, znak in enumerate(tekst):
        if znak.isalpha():
            przesuniecie = int(klucz[i % len(klucz)])
            if znak.islower():
                szyfrowany_znak = chr((ord(znak) - ord('a') + przesuniecie) % 26 + ord('a'))
            else:
                szyfrowany_znak = chr((ord(znak) - ord('A') + przesuniecie) % 26 + ord('A'))
        else:
            szyfrowany_znak = znak
        szyfrogram += szyfrowany_znak
    return szyfrogram

def deszyfruj_gronsfeld(szyfrogram, haslo):
    tekst = ""
    for i, znak in enumerate(szyfrogram):
        if znak.isalpha():
            przesuniecie = int(haslo[i % len(haslo)])
            if znak.islower():
                deszyfrowany_znak = chr((ord(znak) - ord('a') - przesuniecie) % 26 + ord('a'))
            else:
                deszyfrowany_znak = chr((ord(znak) - ord('A') - przesuniecie) % 26 + ord('A'))
        else:
            deszyfrowany_znak = znak
        tekst += deszyfrowany_znak
    return tekst

klucz = input('SZYFRUJ: ')
tekst_jawny = input('Wiadomość: ')
print('Wiadomość: ', tekst_jawny.upper())

# Szyfrowanie
szyfrogram = szyfruj_gronsfeld(tekst_jawny, klucz)
print("Szyfrogram: ", szyfrogram.upper())
# Deszyfrowanie

haslo = input('DESZYFRUJ: ')
print("Odkodowywanie: ", szyfrogram.upper())
if haslo == klucz:
    odszyfrowany_tekst = deszyfruj_gronsfeld(szyfrogram, haslo)
    print("Odszyfrowany tekst:", odszyfrowany_tekst.upper())
else:
    print("Podałeś złe hasło, ty nędzny hakerzyno")






