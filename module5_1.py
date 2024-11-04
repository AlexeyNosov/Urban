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




aist = house ("Aist", 25)
bereg = house ("Bereg", 20)
stolica = house ("Stolica", 55)
bereg.go_to(10)
bereg.go_to(100)
aist.go_to(40)
aist.go_to(5)
stolica.go_to(60)
stolica.go_to(7)