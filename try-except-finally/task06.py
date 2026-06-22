
'''
6. Turlar xatosi (TypeError)
Bitta funksiya yozing, u ikkita qiymatni qabul qilib, ularni ko'paytirsin (a * b). 
Funksiyani chaqirganda bittasiga son, ikkinchisiga esa ro'yxat yoki 
mos kelmaydigan tur bering (masalan: 5 * [2, 3]). TypeError yuz berganda 
"Ushbu ma'lumot turlarini o'zaro ko'paytirib bo'lmaydi" degan matn chiqsin.
'''

def mult(a, b):
    try:
        return a * b
    except TypeError:
        return "Ushbu ma'lumot turlarini o'zaro ko'paytirib bo'lmaydi"
    
def main():
    a = input("Birinchisi: ")
    b = input("Ikkinchisi: ")
    result = mult(a, b)
    print(result)

main()