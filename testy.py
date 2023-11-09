def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                zaszyfrowany_znak = chr((ord(znak) - ord('A') + przesuniecie) % 26 + ord('A'))
            else:
                zaszyfrowany_znak = chr((ord(znak) - ord('a') + przesuniecie) % 26 + ord('a'))
        else:
            zaszyfrowany_znak = znak
        zaszyfrowany_tekst += zaszyfrowany_znak
    return zaszyfrowany_tekst

# Przykład użycia:
tekst_jawny = 'ABC DEF'



zaszyfrowany_tekst = szyfr_cezara(tekst_jawny, przesuniecie)


print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
