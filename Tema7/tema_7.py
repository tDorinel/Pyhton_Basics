# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)

# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria (optional)
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    def __init__(self):
        self.pi = 3.14
    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.__latura = latura
        print(f'In clasa parinte, pi = {self.pi}')

    def aria(self):
        return self.__latura ** 2

    @property
    def latura(self):
        return self.__latura


# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
    def set_latura(self, new_latura):
        self.__latura = new_latura

    @latura.getter
    def get_latura(self):
        return self.__latura

    @latura.deleter
    def del_latura(self):
        self.__latura = None
        print('Am sters latura')

# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        self.__raza = raza
    def aria(self):
        return self.pi*(self.__raza**2)

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def set_raza(self, new_raza):
        self.__raza = new_raza

    @raza.getter
    def get_raza(self):
        return self.__raza

    @raza.deleter
    def del_raza(self):
        self.__raza = None
        print('Raza a fos stearsa')
# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    def descriere(self):
        print('Eu nu am colturi')

# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui

def descriere_interfata(obj):
        obj.descriere()

p1 = Patrat (5)
p1.descriere()
descriere_interfata(p1)

print(f'Latura este de {p1.latura}')
print(f'Aria este de {p1.aria()}')
p1.set_latura(4)
print(f'Noua latura este de {p1.get_latura}')
del p1.del_latura

c1 = Cerc(4)
c1.descriere()
descriere_interfata(c1)
print(f'Raza este {c1.raza}')
print(f'Aria este {c1.aria()}')
c1.set_raza=5
print(f'Noua raza este {c1.get_raza}')
del c1.del_raza


