class Human:
    name = "Julek"
    def whats_your_name(self, welcome = "Czesc", second_name = " Kowalski"):
        return welcome + ", mam na imie " + self.name + second_name

obiect = Human()
print(obiect.name)
print(obiect.whats_your_name("Witam", " Kihler"))
obiect_2 = Human()
obiect_2.name = "Aga"
print(obiect_2.whats_your_name())
print("---------------------------------------------\n\n")

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def whats_your_name(self, welcome = "Czesc"):
        return welcome + ", mam na imie " + self.name + " mam " + str(self.age) + '.'

obiect = Human("Julek", 13)
print(obiect.name)
print(obiect.whats_your_name("Witam"))
obiect_2 = Human("Aga", 35)
obiect_2.name = "Aga"
print(obiect_2.whats_your_name())