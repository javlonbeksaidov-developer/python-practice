
'''
Siz kvadratsiz!

Kvadratlar kvadrati
Sizga qurilish bloklari yoqadi. Ayniqsa, kvadrat shaklidagi qurilish bloklari yoqadi. 
Va sizga eng yoqadigan narsa, ularni kvadrat qurilish bloklari kvadratiga joylashtirishdir!

Biroq, ba'zida ularni kvadrat shaklida joylashtirib bo'lmaydi. Buning o'rniga, siz oddiy to'rtburchakka ega bo'lasiz! 
O'sha portlatilgan narsalar! Agar siz hozir behuda ishlayotganingizni bilishning bir yo'li bo'lsa... Kuting! Bo'ldi! 
Siz shunchaki qurilish bloklaringiz soni mukammal kvadrat ekanligini tekshirishingiz kerak .

Vazifa
Berilgan integral son, uning kvadrat son ekanligini aniqlang :

Matematikada kvadrat son yoki mukammal kvadrat butun sonning kvadratiga teng bo'lgan butun sondir; 
boshqacha qilib aytganda, u o'zi bilan birga bo'lgan biron bir butun sonning ko'paytmasidir.

Sinovlar har doim bir nechta integral sonlardan foydalanadi, 
shuning uchun dinamik tipdagi tillarda bu haqda tashvishlanmang.

Misollar
-1  =>  false
0  =>  true
3  =>  false
4  =>  true
25  =>  true
26  =>  false
'''

def is_square(n):    
    if n == -1 or n < 0:
        return False
    
    if pow(n, 0.5) ** 2 == n:
        return True
    return False