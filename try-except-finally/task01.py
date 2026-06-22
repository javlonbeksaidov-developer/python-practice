
'''
1. Nollga bo'lish (ZeroDivisionError)
Foydalanuvchidan ikkita son so'rang (a va b). 
a / b natijasini hisoblang. Agar foydalanuvchi b o'rniga 0 kiritsa, 
dastur o'chib ketmasdan, "Nollga bo'lish mumkin emas!" degan xabarni chiqarsin.
'''

try:
    a = float(input("Birinchi son: "))
    b = float(input("Ikkinchi son: "))
    c = a / b
    print(f"{a}ni {b}ga bo'lganda {c} chiqadi.")
except ZeroDivisionError:
    print("Xato sonni 0 ga bo'lib bo'lmaydi.")
finally:
    print("Dastur tugadi")