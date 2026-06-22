
'''
7. Har qanday xatoni ovlash (Exception)
Foydalanuvchidan matematik ifoda kiritishni so'rang 
(masalan: 2 + "salom" yoki 10 / 0). Uni eval() funksiyasi yordamida hisoblang. 
Har qanday kutilmagan xato chiqsa, except Exception as e: orqali xatoni ushlab, 
ekranga aniq xato matnini chiqaring.
'''

try:
    ifoda = input("Matematik ifoda kiriting (masalan, 10 / 0 yoki 2 + 'a'): ")
    natija = eval(ifoda)
    print(f"Natija: {natija}")
except Exception as e:
    print(f"Kutilmagan xatolik yuz berdi: {e}")