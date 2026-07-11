"""AMALIYOT
Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin."""


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

    def info(self):
        return f"{self.fname} {self.lname}. {self.year}-yilda to'g'ilgan. Passport: {self.passport}."


class Talaba(Person):
    def __init__(self, fname, lname, year, passport, id, manzil):
        super().__init__(fname, lname, year, passport)
        self.id = id
        self.manzil = manzil
        self.bosqich = 1
        self.fanlar = []

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan)
        else:
            print(f"Bu '{fan}' fani Fanlar classdan emas.")

    def remove_fan(self, fan):
        if isinstance(fan, Fan):
            for i in self.fanlar:
                if fan == i:
                    self.fanlar.remove(fan)
                    print(f"'{fan.get_fan_name()}' fani o'chirildi.")

    def get_fanlar(self):
        return [fan.get_fan_name() for fan in self.fanlar]

    def info(self):
        return f"{self.fname} {self.lname}. {self.year}-yilda to'g'ilgan. Manzili {self.manzil.get_manzil()}da istiqomat qiladi."


class Manzil:
    def __init__(self, viloyat, tuman, mahalla, kocha, uy):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahalla = mahalla
        self.kocha = kocha
        self.uy = uy

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati {self.tuman} tumani {self.mahalla} mahallasi {self.kocha} ko'chasi {self.uy} uy"
        return manzil


class Fan:
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def get_fan_name(self):
        return self.name


class Professor(Person):
    def __init__(self, fname, lname, year, passport, fan, id):
        super().__init__(fname, lname, year, passport)
        self.id = id
        self.fan = fan

    def info(self):
        return f"{self.fname} {self.lname}. {self.year}-yilda to'g'ilgan. {self.fan} fan o'qituvchisi, id raqami: {self.id}"


class Foydalanuvchi(Person):
    def __init__(self, fname, lname, year, passport, username):
        super().__init__(fname, lname, year, passport)
        self.username = username


class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")


pro = Professor("sal", "donu", 2000, "aa1234567", "tarix", 12345678)
# print(pro.info())


talaba_manzil = Manzil(
    "samarqand", "kattaqo'rg'on", "kattaqo'rg'on", "Alisher Navoiy", "6/6"
)

talaba = Talaba("javlon", "saidov", 2005, "AA1234567", 12345678, talaba_manzil)

# print(talaba.info())

fizika = Fan("Fizika")
tarix = Fan("tarix")
matem = "tarix"

# talaba.fanga_yozil(fizika)
# talaba.fanga_yozil(tarix)
# talaba.fanga_yozil(matem)

# talaba.remove_fan(tarix)

# print(talaba.get_fanlar())


print(talaba.get_person_num())