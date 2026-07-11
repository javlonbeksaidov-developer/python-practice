"""AMALIYOT
Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
Obyekt haqida ma'lumot (__rerp__)
Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)
Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling."""

from uuid import uuid4


class Person:
    __person_num = 0

    def __init__(self, fname, lname, year, passport):
        self.fname = fname
        self.lname = lname
        self.year = year
        self.passport = passport
        Person.__person_num += 1

    @classmethod
    def get_person_num(cls):
        return cls.__person_num

    def __repr__(self):
        return f"{self.fname} {self.lname}"


class Talaba(Person):
    def __init__(self, fname, lname, year, passport, manzil):
        super().__init__(fname, lname, year, passport)
        self.__id = uuid4()
        self.manzil = manzil
        self.bosqich = 1
        self.fanlar = []

    def __repr__(self):
        return f"{self.fname} {self.lname}. Id raqami: {self.get_id()}. {self.bosqich}-bosqichda o'qiydi."

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def get_id(self):
        return self.__id

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich

    def __lt__(self, other):
        return self.bosqich < other.bosqich

    def __eq__(self, other):
        return self.bosqich == other.bosqich

    def __le__(self, other):
        return self.bosqich <= other.bosqich


class Manzil:
    def __init__(self, viloyat, tuman, mahalla, kocha, uy):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahalla = mahalla
        self.kocha = kocha
        self.uy = uy

    def __repr__(self):
        return f"{self.viloyat} viloyati {self.tuman} tumani {self.mahalla} mahallasi {self.kocha} ko'chasi {self.uy}-uy"


class Fan:
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def add_students(self, *students):
        for student in students:
            if isinstance(student, Talaba):
                self.talabalar.append(student)
                # print(f"{student.fullname()} {self.name} faniga qo'shildi.")

    def get_students(self):
        return [student for student in self.talabalar]

    def __getitem__(self, key):
        return self.talabalar[key]

    def __setitem__(self, key, value):
        self.talabalar[key] = value

    def __len__(self):
        return len(self.talabalar)

    def __add__(self, other):
        if isinstance(other, Talaba):
            return self.talabalar.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Talaba):
            self.talabalar.remove(other)
        elif isinstance(other, (str, int)):
            for student in self.talabalar:
                if student.get_id() == other or student.passport() == other:
                    self.talabalar.remove(other)

    def __call__(self, *args, **kwds):
        if args:
            for arg in args:
                if isinstance(arg, Talaba):
                    return f"{arg}"
        else:
            return f"{self.name} fani. O'quvchilar soni {len(self.talabalar)} ta"


talaba_1_manzil = Manzil(
    "Samarqand", "Kattaqo'rg'on", "Kattaqo'rg'on", "Alisher Navoiy", "6/6"
)

talaba_1 = Talaba("Javlon", "Saidov", 2005, "AD1234567", talaba_1_manzil)
talaba_2 = Talaba("Ali", "Valiyev", 2000, "AD1234000", talaba_1_manzil)
talaba_3 = Talaba("Hasan", "Husanov", 2009, "AD0004567", talaba_1_manzil)

talaba_2.set_bosqich(3)
talaba_1.set_bosqich(2)

tarix = Fan("Tarix")
matem = Fan("Matematika")
fizika = Fan("Fizika")

tarix.add_students(talaba_1)
matem.add_students(talaba_1, talaba_2, talaba_3)
fizika.add_students(talaba_2, talaba_3)

matem[1] = Talaba("Vali", "Aliyev", 2000, "AD1234000", talaba_1_manzil)

tarix + talaba_2
matem - talaba_3

# print(tarix())
# print(talaba_1)
