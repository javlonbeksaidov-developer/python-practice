
'''
2. Sonni tekshirish (ValueError)
Foydalanuvchidan uning yoshini (int) kiritishni so'rang. 
Agar foydalanuvchi son o'rniga matn (masalan, "yigirma") kiritib yuborsa, 
ValueError ni ushlang va "Iltimos, faqat butun son kiriting!" deb ogohlantiring.
'''

try:
    age = int(input("Yoshingiz: "))
    print(f"Siz {2026 - age}-yilda to'g'ilgan ekansiz.")
except ValueError:
    print("Iltimos, faqat butun son kiriting!")