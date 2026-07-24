"""
Regex PIN kodini tasdiqlash

Bankomatlar 4 yoki 6 xonali PIN kodlarga ruxsat beradi va
PIN kodlar faqat 4 yoki 6 xonali raqamlardan iborat bo'lishi mumkin.

Agar funksiyaga haqiqiy PIN satri uzatilsa, return true, aks holda return false.

Misollar ( Kirish --> Chiqish)
"1234"   -->  true
"12345"  -->  false
"a234"   --> false
"""


def validate_pin(pin):
    # return true or false
    return bool((len(pin) == 4 or len(pin) == 6) and pin.isdigit())
