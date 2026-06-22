
'''
4. Lug'at kalitini topish (KeyError)
Talaba haqida ma'lumot beruvchi lug'at tuzing: 
talaba = {"ism": "Ali", "yosh": 20}. 
Foydalanuvchidan kalit so'z (key) kiritishni so'rang 
(masalan: "ism", "kurs", "manzil"). Agar kiritilgan kalit lug'atda bo'lmasa, 
KeyError ni ushlang va "Bunday ma'lumot topilmadi" deb chiqaring.
'''

try:
    talaba = {
        "ism": "Ali", 
        "yosh": 20
    }

    key = input("Key: ")
    print(talaba[key])
except KeyError:
    print("Bunday ma'lumot topilmadi")