
'''
5. Umidvor Fayl (FileNotFoundError)
Kodingizda matn.txt degan faylni o'qishga (open()) harakat qilib ko'ring. 
Agar kompyuterda bu fayl hali yaratilmagan bo'lsa, 
dastur xato bermasligi uchun FileNotFoundError ni ushlang va "Kechirasiz, 
so'ralgan fayl topilmadi" deb yozing.
'''

try:
    with open("matn.txt", "r") as f:
        matn = f.read()
    print(matn)
except FileNotFoundError:
    print("Kechirasiz, so'ralgan fayl topilmadi")