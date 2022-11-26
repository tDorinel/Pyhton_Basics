'''1. Explicati cu propriile cuvinte, in cadrul unui comentariu, cum functioneaza un if else

Cu ajutorul lui if else putem evalua daca anumite conditii sunt indeplinite,
astfel incat daca acestea sunt indeplinite se va executa codul din if,
daca nu, se va executa codul din else. Exista asadar o ramificare a codului in functie de conditii.'''




#2. Verificati si afisati daca x este numar natural sau nu
x = 5
if x == int(x) and x > 0:
    print(f' {x} este numar natural')
else:
    print(f' {x} nu este numar natural')




# 3. Verificati si afisati daca x este numar pozitiv, negativ sau neutru
x = 0
if x > 0:
    print(f'{x} este numar pozitiv')
elif x < 0:
    print(f'{x} este numar negativ')
elif x == 0:
    print(f'{x} este numar neutru')




#4. Verificati si afisati daca x este intre -2 si 13
x = 10
if x > -2 and x < 13:
    print(f'{x} se afla intre -2 si 13')
else:
    print(f'{x} nu se afla intre -2 si 13')




#5.  Verificati si afisati daca diferenta dintre x si y este mai mica de 5
x = 89
y = 80
if x - y < 5:
    print(f'Diferenta dintre {x} si {y} este mai mica decat 5')
else:
    print(f'Diferenta dintre {x} si {y} nu este mai mica decat 5')



#6. Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)
x = 32
if x not in range(5, 28):
    print(f'{x} nu se afla in intervalul intre 5 si 27')
else:
    print(f'{x}  se afla in intervalul intre 5 si 27')



#7. x si y (int)
# Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare
x = int(25)
y= int(10)
if x == y:
    print(f'{x} si {y} sunt egale')
if x < y:
    print(f'{y} este mai mare decat {x}')
if x > y:
    print(f'{x} este mai mare decat {y}')



#8. X, y, z - laturile unui triunghi
# Afisati daca triunghiul este isoscel, echilateral sau oarecare.
x = int(input('Introduceri lungimea primei laturi'))
y = int(input('Introduceri lungimea celei de-a doua laturi'))
z = int(input('Introduceri lungimea celei de-a treia laturi'))

if x == y and x!= z or y == z and y != x or x == z and z != y :
    print(f'Triunchiul este isoscel')
elif x == y and y == z:
    print(f'Triunghiul este echilateral')
else:
    print(f'Triunghiul este un triunghi oarecare')



# 9. Cititi o literax de la tastatura
# Verificati si afisati daca este vocala sau nu

x = str(input(f'Introduceti o litera de la tastatura'))
if x.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(f'Litera {x} este vocala')
else:
    print(f'Litera {x} nu este vocala')

#Cum pot face in cazul in care inaintea literei se va pune un spatiu? Deoarece, in acest caz codul va merge pe else

'''Transformati si printati notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''
x = int(input('Nota'))
if x >= 9:
    print('A')
elif x >= 8:
    print('B')
elif x >= 7:
    print('C')
elif x >= 6:
    print('D')
elif x >= 4:
    print('E')
else:
    print('F')

# 11.Verificati daca x are minim 4 cifre (x e int)
#(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input('Introduceti un numar de minim 4 cifre'))
x = str(x)
if len(x) >= 4:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

#12. Verificati daca x are exact 6 cifre
if len(x) == 6:
    print(f'{x} are 6 cifre')
else:
    print(f'{x} nu are 6 cifre')

#13. Verificati daca x este numar par sau impar (x e int)
x = int(x)
if x % 2 == 0:
    print(f'{x} este numar par')
else:
    print(f'{x} este numar impar')

#14. x, y, z (int)
#Afisati care este cel mai mare dintre ele?
x = int(input('NR 1'))
y = int(input('NR 2'))
z = int(input('NR 3'))

print(max(x,y,z))

# 15. X, y, z - reprezinta unghiurile unui triunghi
# Verificati si afisati daca triunghiul este valid sau nu
x = int(input('Unhghiul 1: '))
y = int(input('Unghiul 2: '))
z = int(input('Unghiul 3: '))

if x + y + z <= 180:
    print(f'Triunghiul este valid')
else:
    print(f'Triunghiul este invalid')

#16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'.
#Cititi de la tastatura un int x.
#Afisati stringul fara ultimele x caractere.
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti numarul de caractere lipsa'))
print(propozitie[:-x])

#17. Acelasi string.
#Declarati un string nou care sa fie format din primele 5 caractere + ultimele 5
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(len(propozitie))
print(propozitie[:5])
print(propozitie[-5:])

# 18. Acelasi string.
# Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
# (hint: este o functie care va ajuta sa faceti asta).
# Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant.
# output: 'Coral is either the stupidest animal or the smartest '



















