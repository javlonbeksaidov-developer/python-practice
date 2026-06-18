
'''
Pifagor uchligi

3 ta musbat butun sondan iborat tartiblanmagan massiv berilgan bo'lsa , 
ushbu 3 ta butun sondan foydalanib, Pifagor uchligini[ n1, n2, n3 ] hosil qilish mumkinligini aniqlang .

Pifagor uchligi 3 ta butun sonni quyidagicha tartiblashdan iborat:

a 2 + b 2 = c 2

Misollar
[5, 3, 4]: ushbu 3 ta butun son yordamida Pifagor uchligini hosil qilish mumkin : 3 2 + 4 2 = 5 2

[3, 4, 5]: ushbu 3 ta butun son yordamida Pifagor uchligini hosil qilish mumkin : 3 2 + 4 2 = 5 2

[13, 12, 5]: ushbu 3 ta butun son yordamida Pifagor uchligini hosil qilish mumkin : 5 2 + 12 2 = 13 2

[100, 3, 999]: bu 3 ta butun son yordamida Pifagor uchligini hosil qilish MUMKIN EMAS - ularni qanday joylashtirsangiz ham, a 2 + b 2 = c 2 tenglamasini qanoatlantirishning yo'lini hech qachon topa olmaysiz.

Qaytish qiymatlari
Python uchun: qaytarish TrueyokiFalse
JavaScript uchun: return trueyokifalse
Boshqa tillar: Namunaviy testlarni qaytaring 1yoki ularga murojaat qiling.0
'''

# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible

    integers.sort()  
    a, b, c = integers
    return a*a + b*b == c*c