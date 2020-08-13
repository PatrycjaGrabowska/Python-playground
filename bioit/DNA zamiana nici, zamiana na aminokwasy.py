import random
import copy #wykorzystywana do kopiowania nici 

plik = open("NicDna.txt","w")

znaki = ["A", "T", "G", "C"]
kod = [""]
kodkomp = [""]
kodmrna = [""]
n = 100

for znak in range (n):
    znak = random.choice(znaki) #losowe wybieranie jednego znaku z podanej listy
    kod.append(znak) #dodawanie tego znaku do listy
assert znak != "U", "Nie moze byc uracylu"  
assert kod.append(znak) != "U", "nie moze byc uracylu"


plik.write("nic glowna:")
a=' '.join(kod) #polaczenie elementow z listy w string
plik.write("\n" + " 5' "+ a + " 3'")
kodkomp = copy.copy(kod) #kodkomp to nic komplementarna wiec do zamiany potrzebujemy kopii nici glownej, na ktorej pozniej bedziemy pracowac przy zmienianiu znakow 
#nic wygenerowana losowo kopiujemy jako tablice 
assert copy.copy("ATC") == "ATC", "Zle kopiuje"
assert " ".join(["A", "T"]) == "A T", "Zle tworzy lancuch"

plik.write("\n" + "nic komplementarna:")
for znak, i in enumerate(kodkomp): #zamiana elementów listy na przeciwne(komplementarne); enumerate pozwala na odczyt elementu z listy razem z indeksem dzieki temu mozna ograniczyc liczbe zmiennych.
      if i == "A":
          kodkomp[znak] = "T"
      if i == "T":
          kodkomp[znak] = "A"   
      if i == "G":
          kodkomp[znak] = "C"   
      if i == "C":
          kodkomp[znak] = "G"    
assert kodkomp[znak] != "U", "Nie moze byc uracylu" 
assert i != kodkomp[znak], "Nie moze byc to samo"
assert "T" != "G", "Zle zamienia"
assert "T" != "C", "Zle zamienia"
assert "A" != "G", "Zle zamienia"
assert "A" != "C", "Zle zamienia"
assert "G" != "T", "Zle zamienia"
assert "G" != "A", "Zle zamienia"
assert "C" != "A", "Zle zamienia"
assert "C" != "T", "Zle zamienia"
b=' '.join(kodkomp)
plik.write("\n" + " 3' " + b + " 5'")


kodmrna = copy.copy(kod) #kod mRNA to kopia kod - nici glownej 
#zamiana na mRNA
plik.write("\n" + "mRNA:")
 #zamiana elementów T na U
for znak, i in enumerate(kodmrna):
      if i == "T":
          kodmrna[znak] = "U"
assert "A" != "T", "Nie moze byc tyminy"       
c =' '.join(kodmrna) #z listy robimy string
plik.write("\n" + "5' " + c + " 3'" + "\n")#wypisuje elementy listy jako string


RNA= {
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', 
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys', 
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', 
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp', 
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', 
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg', 
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', 
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg', 
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', 
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser', 
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg', 
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', 
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly', 
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', 
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly',
'A' : '---', 'U' : '---', 'G' : '---', 'C' : '---',   
'AA' : '---','AU' : '---','AG' : '---','AC' : '---',
'UA' : '---','UU' : '---','UG' : '---','UC' : '---',
'GA' : '---','GU' : '---','GG' : '---','GC' : '---',
'CA' : '---','CU' : '---','CG' : '---','CC' : '---',
}

#zaczyna szukanie od pierwszego znaku
plik.write("\n" + "tlumaczenie mRNA na aminokwasy:")
plik.write("\n" + "od pierwszej zasady azotowej")
i = 1
idp = 1
idk = 4
kodony=[""]
while i <= len(kodmrna) -1 : #-1 bo nie bierze pod uwage elementu 0
  zasady = ''.join(kodmrna[idp:idk]) #robi stringa z zakresu od id poczatkowego do id koncowego
  plik.write("\n " + zasady +  " " + RNA[zasady])  
  idp += 3 #zwieksza pozycje id poczatkowego o 3 dalej
  idk += 3 #zwieksza pozycje id koncowego o 3 dalej
  i += 3
assert idp != 1, "zle zaczyna"
assert idk != 4, "zle zaczyna"
assert "".join("ATCGAT"[1:4]) == "TCG", "Zle znajduje znaki"

#zaczyna szukanie od drugiego znaku
plik.write("\n" + "od drugiej zasady azotowej")
i = 2
idp = 2
idk = 5
kodony=[""]
while i <= len(kodmrna) -1 :
  zasady = ''.join(kodmrna[idp:idk]) 
  plik.write("\n" + zasady +  " " + RNA[zasady])  
  idp += 3 
  idk += 3 
  i += 3
assert i != 2, "zle zaczyna"
assert idp != 2, "zle zaczyna"
assert idk != 5, "zle zaczyna"
assert "".join("ATCGAT"[2:5]) == "CGA", "Zle znajduje znaki"

#zaczyna szukanie od trzeciego znaku                                     
plik.write("\n" + "od trzeciej zasady azotowej")
i = 3
idp = 3
idk = 6
kodony=[""]
while i <= len(kodmrna) -1 : 
  zasady = ''.join(kodmrna[idp:idk]) 
  plik.write("\n" + zasady +  " " + RNA[zasady])   
  idp += 3 
  idk += 3 
  i += 3
assert i != 3, "zle zaczyna"
assert idp != 3, "zle zaczyna"
assert idk != 6, "zle zaczyna"
assert "".join("ATCGAT"[3:6]) == "GAT", "Zle znajduje znaki"
plik.close()