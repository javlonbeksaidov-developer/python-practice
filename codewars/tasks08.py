"""
Meni zanjirband qil

Umumiy funksiya zanjirini yozing
Boshlang'ich qiymatni qabul qiladigan umumiy funksiya zanjirini va unda bajariladigan funksiyalar massivini (Ruby uchun belgilar massivi) yozing.

Har bir funksiya uchun kirish ma'lumotlari oldingi funksiyaning chiqishidir (boshlang'ich qiymatni o'zining kirish ma'lumotlari sifatida qabul qiladigan birinchi funksiyadan tashqari). Bajarilgandan so'ng yakuniy qiymatni qaytaring.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800
"""


def chain(init_val, functions):
    current_value = init_val

    # Ro'yxatdagi har bir funksiyani ketma-ket chaqiramiz
    for func in functions:
        # joriy qiymatni funksiyaga beramiz va yangi qiymatni saqlaymiz
        current_value = func(current_value)

    return current_value
