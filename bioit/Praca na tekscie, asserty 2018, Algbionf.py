#program odnajdujacy prefixy, sufixy, ćwiczenie assertów
plik1 = open("liczba_wyrazow.txt","w")

tekst = "Ala ma kota \n Ola ma psa \n Kasia chce owce \n"



#obliczanie liczby wyrazow w tekscie
wyrazy = tekst.split(" ") #umozliwia oddzielenie od siebie wyrazow gdy sa przedzielone spacja (tworzy liste wyrazow)
while "\n" in wyrazy :
    wyrazy.remove("\n") #petla pozwala na usuniecie znakow nowej linii i nie doliczania ich w liscie
plik1.write("Liczba wyrazow w tekscie: "+ str(len(wyrazy)))
assert len("Ala") == 3, "Zle liczy"

plik1.close()

plik2 = open("prefiksy.txt","w")
#skladnaie slowa z prefiksow 
plik2.write ("\nprefiks:")
k = 2
for wyraz in wyrazy:
     w = ''.join(wyraz[0:k]) #zamienia liste w string
     plik2.write(w)
assert len(wyraz) > k, "nie mozna stworzyc prefiksu wyrazu"
assert " ".join(["ma", "kota"]) == "ma kota", "Zle tworzy lancuch"
assert "Ala"[0:2] == "Al", "Zle liczy prefiks"
plik2.close()

plik3 = open("sufiksy.txt","w")
#skladanie slowa z sufiksow
plik3.write("\nsufiks:")
for wyraz in wyrazy:
    d = len(wyraz)
    s = ''.join(wyraz[d-2:d]) #bierze dwa ostatnie znaki kazdego wyrazu i zmienia je w string
    plik3.write("" + s ) 
assert d == len(wyraz), "zle liczy"
assert "Kasia"[len("Kasia")-2 : len("Kasia")] == "ia", "Zle tworzy sufiks"
plik3.close()

plik4 = open("najdluzsze_slowo.txt","w")
plik4.write ("\nnajdluzsze slowo:")
plik4.write( (max(wyrazy, key = len))) #max pozwala na znalezienie najwiekszego wyrazu jesli chodzi o dlugosc (key = len)
assert max(["ala", "i"], key = len) == "ala", "zle znajduje najdluzsze slowo"
plik4.close()

plik5 = open("najkrotsze_slowo.txt","w")
plik5.write("\nnajkrotsze slowo:")
plik5.write((min(wyrazy, key = len))) #min szuka minimalnego gdzie key - kluczem wg ktorego szukamy jest dlugosc (len)
assert  min(['ala', 'i'], key=len) == 'i',  ' zle wyznacza najkrotsze slowo'
plik5.close()

plik6 = open("sort_alf.txt","w")
plik6.write("\nsortowanie alfabetyczne")
l = sorted(wyrazy, key = str.lower) #kluczem wg ktorego szukamy jest ciag znakow od najmniejszego
assert sorted(["Ala", "Kasia"], key = str.lower) == ["Ala", "Kasia"], "Zla kolejnosc"
plik6.write(str(l))
plik6.close()

plik7 = open("dlugos_slow.txt","w")
plik7.write("\nsortowanie wg. dlugosci slow")
a = sorted(wyrazy, key=len)
assert sorted(["ma","kota"], key = len) == ["ma", "kota"]
plik7.write(str(a))
plik7.close()