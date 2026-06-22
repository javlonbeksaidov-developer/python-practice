
'''
8. finally bilan hisobot
Foydalanuvchidan biror son kiritishni so'rang va uni kvadratga oshiring. 
Kodda try, except va finally bloklaridan foydalaning. Xato bo'lishi yoki 
bo'lmasligidan qat'i nazar, finally bloki ichida "Dastur ishi yakunlandi, 
e'tiboringiz uchun rahmat!" degan yozuv chiqsin.
'''

try:
    son = float(input("Son: "))
    print(f"{son} sonining kvadrati {son * son} songa teng")
except Exception as xato:
    print(xato)
finally:
    print("Dastur ishi yakunlandi, e'tiboringiz uchun rahmat!")