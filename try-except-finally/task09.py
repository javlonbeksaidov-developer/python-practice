
'''
9. Ketma-ket except bloklari
Foydalanuvchidan ro'yxat indeksini so'raydigan kod yozing. 
Unda bir vaqtning o'zida ham ValueError (agar son o'rniga harf kiritsa), 
ham IndexError (agar katta son kiritsa) xatolarini 
alohida-alohida exceptlar bilan ushlang.
'''

try:
    raqamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = int(input("index: "))
    print(raqamlar[index])
except ValueError:
    print("Xato. Faqat butun son kiriting.")
except IndexError:
    print("Xato. Index qiymati oshib ketdi.")