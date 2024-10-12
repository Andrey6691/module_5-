class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


First = House('First', 20)
Second = House('Second', 10)
# __str__
print(First)
print(Second)

# __len__
print(len(First))
print(len(Second))
