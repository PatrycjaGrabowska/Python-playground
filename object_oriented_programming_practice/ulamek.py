class Ulamek():
    
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    
    def wypisz(self):
        print(f"{self.licznik}/{self.mianownik}")
    
    def NWD(self):
        
        while self.licznik != self.mianownik:

            if self.licznik > self.mianownik:
                self.licznik = self.licznik - self.mianownik
                
            if self.licznik < self.mianownik:
                self.mianownik = self.mianownik - self.licznik
       
        return self.licznik    
                
        
    def skroc(self):
        
        if self.mianownik % self.licznik == 0:
              
              self.mianownik = self.mianownik / self.licznik
              self.licznik = 1
              return (Ulamek(self.licznik, self.mianownik))
            
        elif self.mianownik % self.licznik != 0:
             dzielnik = Ulamek(self.licznik, self.mianownik).NWD()
             self.licznik = self.licznik / dzielnik
             self.mianownik = self.mianownik / dzielnik
             return (self.licznik, self.mianownik)
         
    def dodaj(u1, u2):
        
        if u1.mianownik == u2.mianownik:
            
            wynik = Ulamek(u1.licznik + u2.licznik , u1.mianownik)
            wynik.skroc()
            
        else:

            wynik = Ulamek((u1.licznik * u2.mianownik + u2.licznik * u1.mianownik), (u1.mianownik * u2.mianownik))
            wynik.skroc()
            
        return wynik
            
    def odejmij(u1, u2):
        
        if u1.mianownik == u2.mianownik:
            
            wynik = Ulamek(u1.licznik - u2.licznik , u1.mianownik)
            wynik.skroc()
            
        else:

            wynik = Ulamek((u1.licznik * u2.mianownik - u2.licznik * u1.mianownik), (u1.mianownik * u2.mianownik))
            wynik.skroc()
            
        return wynik
    
    def mnoz(u1, u2):
        nowy_licznik = u1.licznik * u2.licznik
        nowy_mianownik = u1.mianownik * u2.mianownik
        return Ulamek(nowy_licznik, nowy_mianownik).skroc()
        
    def dziel(u1, u2):
        wynik = Ulamek(u1.licznik * u2.mianownik, u1.mianownik * u2.licznik)
        wynik.skroc()
        return wynik       
       # nowy_licznik = u1.licznik * u2.mianownik
        #nowy_mianownik = u1.mianownik * u2.licznik
        #wynik = Ulamek(nowy_licznik, nowy_mianownik)
        #return wynik.skroc()
    
def main():
    a = Ulamek(2, 4)
    a.skroc()
    a.wypisz()
    
    b = Ulamek(20, 24)
    b.skroc()
    b.wypisz()
    
    u1 = Ulamek(3, 4)
    u2 = Ulamek(1, 6)
    
    Ulamek.dodaj(u1,u2).wypisz()
    Ulamek.odejmij(u1,u2).wypisz()
    Ulamek.mnoz(u1,u2).wypisz()
    Ulamek.dziel(u1,u2).wypisz()
    
    
    
    
    
if __name__ == "__main__":
    main()