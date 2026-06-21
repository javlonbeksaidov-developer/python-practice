
'''
Elementni tekshirish (in): {"olma", "banan", "anor"} to'plami bor. 
Foydalanuvchidan meva nomini so'rang. Agar u kiritgan meva to'plam ichida bo'lsa, 
"Bazada bor", aks holda "Bazada yo'q" deb chiqaring.
'''

mevalar = {"olma", "banan", "anor"}
meva = input("Meva: ")
if meva in mevalar:
    print("Bazada bor")
else:
    print("Bazada yo'q")