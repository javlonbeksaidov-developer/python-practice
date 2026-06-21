
'''
Elementni o'chirish: 5 ta har xil sonlardan iborat ro'yxat yarating. 
Ro'yxatdagi 2-indeksda turgan sonni .pop() yoki del yordamida 
o'chirib tashlang va yangi ro'yxatni ko'ring.
'''

import random

sonlar = random.sample(range(10, 101), 5)
print(sonlar)

# del sonlar[2]
a = sonlar.pop(2)

print(sonlar, a)
