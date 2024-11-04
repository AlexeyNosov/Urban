class house:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_flours = int(number_of_flours)
    def go_to(self, flour):
        if flour > self.number_of_flours:
            print (f"В ЖK {self.name} нет такого этажа ({flour}), а всего {self.number_of_flours}")
        else:
            print (f"В ЖК {self.name} едем на этаж {flour}")
            for i in range(1, flour + 1):
                print(f"Этаж {i}")
    def __len__(self):
        return self.number_of_flours
    def __str__(self):
        return (f"Название ЖК {self.name}, заявленное количество этажей {self.number_of_flours}")
    def __del__(self):
        print(f"Продажи в ЖК {self.name} прекращены")

aist = house ("Aist", 25)
bereg = house ("Bereg", 20)
stolica = house ("Stolica", 55)

print(str(aist))
print(str(bereg))
print(str(stolica))
print (f"Измереная высота ЖК {stolica.name} {len(stolica)} этажей")
print (f"Измереная высота ЖК {aist.name} {len(aist)} этажей")
print (f"Измереная высота ЖК {bereg.name} {len(bereg)} этажей")
input("Нажмите любую клавишу")


