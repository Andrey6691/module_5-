class House:
    __instance = None
    houses_history = []


    def __new__(cls, *args, **kwargs):
        if args:            # Проверка args: Если переданы аргументы, извлекается первый аргумент name (название дома).
            name = args[0]
        cls.houses_history.append(name)  # Добавление в историю: Название дома добавляется в список cls.houses_history.
        return super().__new__(cls)      # Создание объекта: Вызывается super().new(cls),
                                           # чтобы создать новый экземпляр класса House.

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 30)
print(House.houses_history)

# # Удаление объектов
del h2
del h3

print(House.houses_history)



