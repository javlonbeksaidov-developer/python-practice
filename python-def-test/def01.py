
'''1. Oddiy usul: assert kalit so'zi
assert — bu berilgan shartning rost (True) ekanligini tekshiradi. Agar shart yolg'on (False) bo'lsa, Python xatolik (AssertionError) beradi.'''

def qoshish(a, b):
    return a + b

# Tekshirish
assert qoshish(2, 3) == 5
assert qoshish(-1, 1) == 0
assert qoshish(0, 0) == 0

print("Barcha assert testlar muvaffaqiyatli o'tdi!")