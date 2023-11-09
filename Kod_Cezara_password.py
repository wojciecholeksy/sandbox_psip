def kod_cezara(tekst):
    przesuniety_tekst = ''
    for znak in tekst:
        if znak.isalpha():
            if znak.islower():
                przesuniety_znak = chr((ord(znak) - ord('a') + 3) % 26 + ord('a'))
            else:
                przesuniety_znak = chr((ord(znak) - ord('A') + 3) % 26 + ord('A'))
        else:
            przesuniety_znak = znak
        przesuniety_tekst += przesuniety_znak
    return przesuniety_tekst
tekst_do_przesuniecia = "\nABC DEF\nTERA EST ROTUNDA"

przesuniety_tekst = kod_cezara(tekst_do_przesuniecia.upper())

print("Input: ", tekst_do_przesuniecia.upper() )
print("Output: ", przesuniety_tekst.upper())