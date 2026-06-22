
'''
10. Kuchaytirilgan bo'lish amali
Foydalanuvchidan ikkita son so'rang. Birinchi sonni ikkinchisiga bo'ling. 
Kodda try, except ZeroDivisionError, except ValueError va 
eng oxirida baribir ishlaydigan finally bloklarini birgalikda ishlating.
'''

try:
    a = int(input("1-son: "))
    b = int(input("2-son: "))

    c = a / b
    print(c)
except ZeroDivisionError:
    print("Son 0 ga bo'linmaydi.")
except ValueError:
    print("Faqat butun son.")
finally:
    print("Dastur tugadi. The end.")