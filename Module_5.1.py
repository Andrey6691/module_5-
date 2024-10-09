class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for i in range(1, new_floor+1):
            if new_floor > self.number_of_floors:
                return print("Такого этажа не существует")
            else:
                print(i)



First = House('First', 15)
Second = House ('Second', 5)
First.go_to(15)
Second.go_to(6)

