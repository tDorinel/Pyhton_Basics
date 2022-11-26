''' 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a) afiseaz-o
b) Inverseaza ordinea folosind slicing si suprascrie aceasta lista
c) Printeaza varianta actuala (inversata)
d) Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
3) Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala'''

note_muzicale = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si','do')
print(note_muzicale)

note_muzicale[::-1]
note_muzicale = note_muzicale[::-1]
print(note_muzicale)

reversed(note_muzicale)
print(note_muzicale)
#Aici ar fi trebuit sa ajung inapoi la varianta initiala, insa nu imi dau seama cum...

#2. De cate ori apare ‘do’?
note_muzicale.count('do')
print(note_muzicale.count('do'))

#3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#Gasiti 2 variante sa le uniti intr-o singura lista.
x = [3,1,0,2]
y = [6,5,4]

z = x+y
print(z)

(x.extend(y))
print(x)

#4. Sortati si afisati lista generata la ex anterior
#Stergeti numarul 0 folosind o functie
#Afisati iar lista
x = [3,1,0,2]
y = [6,5,4]
z = x+y

z.sort()
print(z)

z.remove(0)
print(z)

#5. Folosind un if verificati lista generata la ex3 si afisati
#Lista este goala
#Lista nu este goala

if len(z) == 0:
    print(f'Lista este goala')
else:
    print(f'Lista nu este goala')

#6. Folositi o functie care sa goleasca lista de la ex3
z.clear()
print(z)
#SAU
z *= 0
print(z)

#7. Copy paste la ex 5. Verificati inca o data.
#Acum ar trebui sa se afiseze ca lista e goala
if len(z) == 0:
    print(f'Lista este goala')
else:
    print(f'Lista nu este goala')

#8.  Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(list(dict1.keys()))

#9. Printati cei 3 elevi si notele lor
#Ex: ‘Ana a luat nota {x}’
#Doar nota o veti lua folosindu-va de cheie
elev = 'Ana'
print(f'{elev} a luat nota {dict1[elev]}')

elev = 'Gigel'
print(f'{elev} a luat nota {dict1[elev]}')

elev = 'Dorel'
print(f'{elev} a luat nota {dict1[elev]}')

#10. Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare
dict1['Dorel'] = 6
print(dict1)
print(dict1['Dorel'])

#11. Gigel se transfera din clasa
#Cautati o functie care sa il stearga
#Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi
del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9
print(dict1)

#12.Set
#zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#Adaugati in zilele_sapt ‘luni’
#Afisati zile_sapt. Ce observati?
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
# La prima vedere se poate observa o rearanjare a termenilor

#13.Folositi un if si verificati daca
#Weekend este un subset al zilelor din sapt
#Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print(f'Weekend este subset al zilelor din saptamana')
else:
    print(f'Weekend nu este subset al zilelor din saptamana')


#14. Afisati diferentele dintre aceste 2 seturi
diferente = zile_sapt - weekend
print(diferente)
#SAU
print(zile_sapt.difference(weekend))

#15.Afisati intersectia elementelor din aceste 2 seturi
elemente_comune = zile_sapt & weekend
print(elemente_comune)
#SAU
print(zile_sapt.intersection(weekend))







