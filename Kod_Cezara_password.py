def kod_cezara(tekst):
    przesuniety_tekst = ''
    for znak in tekst:
        if znak.isalpha():
            if znak.islower():
                przesuniety_znak = chr((ord(znak) - ord('a') + 1) % 26 + ord('a'))
            else:
                przesuniety_znak = chr((ord(znak) - ord('A') + 1) % 26 + ord('A'))
        else:
            przesuniety_znak = znak
        przesuniety_tekst += przesuniety_znak
    return przesuniety_tekst
tekst_do_przesuniecia = input("Podaj wiadomość do zakodowania: ")
przesuniety_tekst = kod_cezara(tekst_do_przesuniecia)

print("Oryginalny tekst", tekst_do_przesuniecia)
print("Przesunięty tekst", przesuniety_tekst)