from uuid import uuid4


class Auto:
    __num_auto = 0

    def __init__(self, make, model, rang, yil, narx, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Auto.__num_auto += 1

    def __repr__(self):
        return f"Auto: {self.make} {self.model}"


class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.autos = []

    def __repr__(self):
        return f"'{self.name}' avtosalon"

    def add_auto(self, *autos):
        for auto in autos:
            if isinstance(auto, Auto):
                self.autos.append(auto)
                print(f"{auto} mashina qo'shildi.")
            else:
                print("Qiymat xato!")

    def get_cars(self):
        return self.autos

    def __len__(self):
        return len(self.autos)

    def __getitem__(self, key):
        return self.autos[key]

    def __setitem__(self, key, value):
        self.autos[key] = value


car_1 = Auto("GM", "Malibu", "qora", 2020, 40000, 1000)
car_2 = Auto("GM", "Spark", "oq", 2022, 15000, 3500)

avtosalan = AutoSalon("Rental CARS")

avtosalan.add_auto(car_1)
avtosalan.add_auto(car_2)

# print(avtosalan.get_cars())

# print(len(avtosalan))

print(avtosalan[1])

avtosalan[1] = Auto("GM", "Nexia", "qizil", 2018, 30000, 1200)
print(avtosalan.get_cars())
