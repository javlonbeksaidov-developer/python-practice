
'''
3. Ro'yxat indeksi (IndexError)
Meva nomlaridan iborat 3 ta elementli ro'yxat tuzing (['olma', 'banan', 'anor']). 
Foydalanuvchidan indeks (son) so'rang va o'sha indeksdagi mevani chiqaring. 
Agar foydalanuvchi 5 yoki 10 kabi yo'q indeksni kiritsa, IndexError ni ushlab, 
"Bunday indeksli meva mavjud emas" deb chiqaring.
'''

try:
    mevalar = ['olma', 'banan', 'anor']
    index = int(input("index: "))
    print(mevalar[index - 1])
except IndexError:
    print("Bunday indeksli meva mavjud emas")