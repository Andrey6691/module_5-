class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors == number_of_floors

    def __add__(self, value):
        self.value = value if isinstance(value, int) else self.number_of_floors
        self.number_of_floors = self.number_of_floors + value
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return self

    def __iadd__(self, value):
        self.value = value if isinstance(value, int) else self.number_of_floors
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.value = value if isinstance(value, int) else self.number_of_floors
        self.number_of_floors = value + self.number_of_floors
        return self

    def __lt__(self, other):#<
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors < number_of_floors



    def __le__(self, other): #<=
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors <= number_of_floors

    def __gt__(self, other): #  >
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors > number_of_floors


    def __ge__(self, other): # >=
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors >= number_of_floors

    def __ne__(self, other): # !=
        number_of_floors = other if isinstance(other, int) else other.number_of_floors
        return self.number_of_floors != number_of_floors



F = House('First', 10)
S = House('Second', 20)

print(F)
print(S)


print(F == S) # __eq__

F = F + 10 # __add__
# print(First)
print(F == S)

F += 10 # __iadd__
print(F)

S = 10 + S # __radd__
print(S)
#
print(F > S) # __gt__
print(F >= S) # __ge__
print(F < S) # __lt__
print(F <= S) # __le__
print(F != S) # __ne__