# C06_EX02:  Creati un fisier rectangle.py in care sa va definiti o clasa Rectangle, care are 2 atribute width si length,
# instantiate in cadrul constructorului cu 2 valori integer.
# a) Pentru clasa respectiva creati o functie get_area care returneaza aria dreptunghiului.
# b) Creati si o functie display care afiseaza dreptunghiul folosind un parametru optional pentru a desena; in cazul in care
# parametrul nu este dat, se foloseste ca default caracterul *.
# c) Creati un fisier nou test_rectangle.py unde sa va importati clasa Rectangle (din rectangle.py) si testati codul.
# Exemplu de rulare:
# new_rectangle = Rectange(2, 4)
# print(new_rectangle.get_area()) => 8
# new_rectangle.display() => ****     sau: new_rectangle('#') => ####
#                            ****                                ####


class Rectangle:
    def init(self, input_width, input_length):
        self.width = input_width
        self.length = input_length

    def get_area(self):
        return self.width * self.length

    def display(self):
        for _ in range(self.width):
            print('', self.length)