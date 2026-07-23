'''2-mashq: Xatoliklarni ushlash (pytest.raises)
Topshiriq: Parolning mustahkamligini tekshiradigan funksiya yozing va noto'g'ri parollarda maxsus xatolik qaytarayotganini testlang.

Funksiya: parolni_tekshir(parol: str)
Parol uzunligi kamida 8 ta belgidan iborat bo'lishi kerak.
Kamida 1 ta raqam qatnashgan bo'lishi kerak.
Aks holda ValueError xatoligini berishi kerak.
Kutilayotgan testlar:
To'g'ri parol berilganda True qaytarishi.
Uzunligi 8 dan kichik bo'lsa ValueError berishi (pytest.raises bilan tekshiring).
Ichida raqam bo'lmasa ham ValueError berishi.'''

def check_password(password):
    if len(password) < 8:
        raise ValueError("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")

    if not any(belgi.isdigit() for belgi in password):
        raise ValueError("Parolda kamida 1 ta raqam bo'lishi kerak!")

    return True


def main():
    password = input('Password: ')
    if check_password(password):
        print("Tasdiqlandi.")
    else:
        print("Xato")

if __name__ == '__main__':
    main()