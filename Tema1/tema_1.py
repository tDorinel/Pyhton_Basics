''' 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
O variabila este o zona din memorie care stoecheaza datele.
Variabila este asemenea unei cuti in care depozitam o anumita informatie'''

'''2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă:

- string
- int
- float
- bool
'''

#variabila string
tip_carte = 'beletristica'

#variabila int
numar_pagini = 268

#variabila float
pret = 29.99

#variabila bool
imi_place = True

#3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(tip_carte))

print(type(numar_pagini))

print(type(pret))

print(type(imi_place))

#4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
round(pret)
print(round(pret))

pret=round(pret)
print(pret)

#Verifica tipul acesteia
type(pret)
print(type(pret))

#5. 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
#Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Aceasta este o carte de tip {tip_carte}')
print(f'Fiind o carte de {tip_carte} are un numar de {numar_pagini} de pagini')
print(f'Pretul acestei carti este de {pret} lei')
print(f'Cumpar cartea: {imi_place}')

#6. Citește de la tastatură:
#numele;
#prenumele.
#Afișează: 'Numele complet are x caractere'.'''
numele = input('Introduceti numele dumneavoastra')
prenumele = input('Introduceti prenumele dumneavoastra')
print(f'Ati intrdous numele {numele}')
print(f'Ati introuds prenumele {prenumele}')

len(numele)
print(f'Numele complet are {len(numele)} caractere')

# Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
lungimea = int(input('Scrieti aici lungimea'))
latimea = int(input('Scrieti aici latimea'))

print(f'Aria dreptunghiului este {lungimea*latimea}')

#8. Având stringul:
Propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(Propozitie.count(' the '))

#9.Acelasi string
print(Propozitie.count(' the '))

#10. Folosește un assert ca să verifici dacă acest string conține doar numere.
print(Propozitie.isdigit())
print(Propozitie.isnumeric())
# Un assert este o validare

