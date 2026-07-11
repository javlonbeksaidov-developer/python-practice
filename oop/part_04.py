from uuid import uuid4
from part_03 import Person

class Auto:
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Auto.__num_avto += 1

    def get_id(self):
        return self.__id

    def get_km(self):
        return self.__km

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Kilometrni kamaytirib bo'lmaydi.")

    @classmethod
    def get_num_auto(cls):
        return cls.__num_avto


avto_1 = Auto("GM", "Malibu", "qora", 2020, 20000, 1000)
print(avto_1.get_id())
print(avto_1.get_km())

avto_1.add_km(1000)
print(avto_1.get_km())

print(avto_1.get_num_auto())


odam = Person('javlon', 'saidov', 2005, 'aa1234567')