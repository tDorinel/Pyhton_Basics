#1.Avand lista
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#Folositi un for ca sa iterati prin toata lista cu ajutorul indexilor si sa afisati
#‘Masina mea preferata este x’
#Faceti acelasi lucru cu un for each
#Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#a)
for i in range(len(masini)):
    print(f"Masina mea preferata este {masini[i]}")

#b).
for masina in masini:
    print(f"Masina mea preferata este {masina}")

#c).
i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i += 1


#2. Aceeasi lista
#Folositi un for in for
#   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul (v1 - caracter, v2 - element)
#Printati varianta finala a listei
#Incercati sa rezolvati atat v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
#Cat si v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
#v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']

#v1
for i,m in enumerate(masini):
    masini[i] = m[0].lower() + m[1:-1].upper() + m[-1].lower()
print(masini)

#v2
for i in range(len(masini)):
    if i in (0,len(masini)-1):
        masini[i] = masini[i].lower()
    else:
        masini[i] = masini[i].upper()
print(masini)

#2.1. Aceeasi lista
#Folositi un for in for
#v1. cu for in for
for i in range(len(masini)):
    masina_modif = ''
    for j in range(len(masini[i])):
        if j in (0, len(masini[i])-1):
            masina_modif += masini[i][j].lower()
        else:
            masina_modif += masini[i][j].upper()
    masini[i] = masina_modif
print(masini)

#v2.
for i in range(len(masini)):
    if i == 0 or i == len(masini) - 1:
        masini[i] = masini[i].lower()
    else:
        masini[i] = masini[i].upper()
print(masini)

#Aceeasi lista,
#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea cu for
#Daca masina e mercedes (if)
#   Printam ‘am gasit masina dorita de dvs’
#   Iesim din ciclu folosind un cuvant cheie care face acest lucru
#Altfel:
#   Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina cautata de cumparator')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

# 4. Aceasi lista.
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

for masina in masini:
    if masina in ('Trabant', 'Lastun'):
        continue
    print(f"S-ar putea sa va placa masina {masina}")

# 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini.
# Cand gasiti Lastun sau Trabant:
#     Salvati aceste masini in masini_vechi
#     Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for i in range(len(masini)):
    if masini[i] in ('Trabant', 'Lastun'):
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(masini_vechi)
print(masini)


# 6. Avand dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {
     'Dacia': 6800,
     'Lastun': 500,
     'Opel': 1100,
     'Audi': 19000,
     'BMW': 23000
}

for masina, pret  in pret_masini.items():
    if pret < 15000:
        print(f'Puteti achizitiona masina {masina}')


#7. Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

numerotare = 0
for n in numere:
    if n == 3:
        numerotare += 1
print(f'Numarul 3 apare de {numerotare} ori')

# 8. Aceeasi lista. Iterati prin ea.
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

suma = 0
for z in numere:
    suma += z
print(f'Suma numerelor din lista este {suma}')

#9. Aceeasi lista. Iterati prin ea.
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

#V1
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for c in range(len(numere)-1):
    if numere[c] > numere[c+1]:
        numere[c], numere[c+1] = numere [c+1], numere[c]
print(numere[-1])

#V2
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]
for b in numere:
    if b > maxim:
        maxim = b
print(maxim)

# 10. Aceeasi lista. Iterati prin ea.
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for h in range(len(numere)):
    if numere[h] > 0:
        numere[h] = -numere[h]
print(numere)


# 11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for u in alte_numere:
    if u % 2 == 0:
        numere_pare.append(u)
    else:
        numere_impare.append(u)
    if u > 0:
        numere_pozitive.append(u)
    else:
        numere_negative.append(u)
print(f"Numere pare:     {numere_pare}")
print(f"Numere impare:   {numere_impare}")
print(f"Numere pozitive: {numere_pozitive}")
print(f"Numere negative: {numere_negative}")





