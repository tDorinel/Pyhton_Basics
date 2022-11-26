# 1. Functie care sa calculeze si sa returneze suma a 2 numere
def sum(a,b):
    return a+b

print(sum(11,73))

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def check(nr):
    return nr % 2 == 0

print(check(9))

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
def count_letters(nume, prenume, nume_mijlociu):
    return len(nume+prenume+nume_mijlociu)

print(count_letters('Todoran', 'Dorinel','Vasile'))

# 4. Functie care returneaza aria dreptunghiului
def aria(width, lenght):
    return width*lenght

print(aria(10, 15))

# 5. Functie care returneaza aria cercului
from pi_values import pi
def aria_cerc(raza):
    return pi*raza**2

print(aria_cerc(5))

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def finder(letter, string):
    return letter in string

print(finder('e', 'My name is'))

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y

def counter(string):
    counter_letters = {'lower':0, 'upper':0}
    for x in string:
        if x.isupper():
            counter_letters['upper'] +=1
        elif x.islower():
            counter_letters['lower'] +=1
    return counter_letters

print(counter('TelEVIzor'))


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def positive_list(lst):
    positive_of_numbers_list = []
    for n in lst:
        if n > 0:
            positive_of_numbers_list.append(n)

    return positive_of_numbers_list

print(positive_list([2,10,-8,-20,-14]))


# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale

def check_numbers(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif x<y:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print(f'Numerele sunt egale')

print(check_numbers(3,5))

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def adding_numbers(n, number_set):
    if n in number_set:
        print(f'Nu am adaugat numarul {n} in set. Acesta exista deja')
        return False
    else:
        number_set.add(n)
        print(f'Am adaugat numarul nou {n} in set')
        return True

print(adding_numbers(8, {10,5,2,9,29}))

# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
def month_number_days(month):
    return monthrange(2022, month)[1]

print(month_number_days(10))

# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere

# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

def calculator(x,y):
    return x+y, x-y, x*y, x/y

a, b, c, d = calculator(5,6)
print('Suma:', a)
print('Diferenta', b)
print('Inmultire', c)
print('Impartire', d)


