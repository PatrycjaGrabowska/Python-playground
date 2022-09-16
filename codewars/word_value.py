import string

def words_to_marks(s):

    slowo = list(s)
    lista = list(string.ascii_lowercase)
    slownik = {}
    wartosc = 1
    x = 0
    for i in lista:
        slownik[lista[x]] = wartosc
        x = x + 1
        wartosc = wartosc + 1

    suma = 0
    for litera in slowo:
        if litera in slownik:
            wartosc_litery = slownik.get(litera)
            suma += wartosc_litery


    return suma
