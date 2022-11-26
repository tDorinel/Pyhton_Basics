#Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

#1. Clasa Cerc
#Atribute: raza, culoare
#Constructor pt ambele atribute
#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria
#diametru()
#circumferinta()
from pi_values import pi
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descriere_cerc(self):
        print(f'Cercul este de culoare {self.culoare}')

    def aria(self):
        return self.raza**2*pi

    def diametru(self):
        return self.raza*2

    def circumferinta(self):
        return self.raza*2*pi


c1 = Cerc(5, 'albastra')
c2 = Cerc(10, 'verde')

c1.descriere_cerc()
c2.descriere_cerc()
print(c1.aria())
print(c2.aria())
print(c1.diametru())
print(c2.diametru())
print(c1.circumferinta())
print(c2.circumferinta())



#Clasa Dreptunghi
#Atribute: lungime, latime, culoare
#Constructor pt toate atributele
#Metode:
#descrie()
#aria()
#perimetrul()
#schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea dreptunghiului  {self.lungime} cm, latimea  {self.latime} cm  culoare {self.culoare}')

    def aria(self):
        return self.lungime * self.latime

    def permetrul(self):
        return 2*self.lungime + 2*self.latime

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(4, 2, 'portocalie')
d2 = Dreptunghi(10, 5, 'rosie')


d1.descrie()
d2.descrie()
print(d1.aria())
print(d2.aria())
print(d1.permetrul())
print(d2.permetrul())

d1.schimba_culoare('roz')
d2.schimba_culoare('mov')

d1.descrie()
d2.descrie()

#Clasa Angajat
#Atribute: nume, prenume, salariu
#Constructor pt toate atributele
#Metode:
#descrie()
#nume_complet()
#salariu_lunar()
#salariu_anual()
#marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'{self.nume} {self.prenume} are salariu de {self.salariu}')

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este {self.salariu}')

    def salariu_anual(self):
        print(f'Salariul anual al angajatului este {self.salariu*12}')

    def marire_salariu(self, procentaj):
        marire_salariala= self.salariu*procentaj/100
        self.salariu = self.salariu + marire_salariala
        print(f'Dupa marire, salariul angajatului {self.nume} {self.prenume} este de {self.salariu}')




angajat1 =  Angajat('Todoran', 'Dorinel', 2500)
angajat2 = Angajat('Gliga', 'Marian', 4500)

angajat1.descrie()
angajat2.descrie()
angajat1.nume_complet()
angajat2.nume_complet()
angajat1.salariu_lunar()
angajat2.salariu_lunar()
angajat1.salariu_anual()
angajat2.salariu_anual()
angajat1.marire_salariu(10)
angajat2.marire_salariu(20)



#4.Clasa Cont
#Atribute: iban, titular_cont, sold
#Constructor pentru toate
#Metode:
#afisare_sold() - Titularul x are in contul y suma de n lei
#debitare_cont(suma)
#creditare_cont(suma)

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma_debitata):
        print(f'Contul {self.iban} detinut de {self.titular_cont} a fost debitat cu suma de {suma_debitata}')


    def creditare_cont(self, suma_creditata):
        print(f'Contul {self.iban} detinut de {self.titular_cont} a fost creditat cu suma de {suma_creditata}')

#????????
#   def afisare_sold_sfarsitul_lunii(self):
#       print(f'Soldul contului {self.iban} detinut de {self.titular_cont} este de {sold_nou}')


cont1 = Cont('RO2965102985', 'Todoran', 4000)
cont2 = Cont('RO2821709802', 'Marian', 1000)


cont1.afisare_sold()
cont2.afisare_sold()
cont1.debitare_cont(2500)
cont2.debitare_cont(4500)
cont1.creditare_cont(1000)
cont2.creditare_cont(4000)
#cont1.afisare_sold_sfarsitul_lunii()
#cont2.afisare_sold_sfarsitul_lunii()








