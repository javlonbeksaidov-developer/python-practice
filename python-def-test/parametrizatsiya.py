'''3-mashq: Parametrizatsiya (@pytest.mark.parametrize)
Topshiriq: Berilgan yil kabisa yili (leap year) yoki yo'qligini aniqlovchi funksiyani bitta test funksiya ichida ko'plab qiymatlar bilan tekshiring.
Qoida: Yil 4 ga bo'linsa kabisa yili, lekin 100 ga bo'linib 400 ga bo me'da bo'lsa kabisa emas. (Masalan: 2000 — kabisa, 1900 — kabisa emas, 2024 — kabisa).
Kutilayotgan test: @pytest.mark.parametrize yordamida kamida 5 xil yilni (kabisa va kabisa bo'lmagan) bitta testda sinab ko'ring.
'''

def kabisa(year):
    return bool(year >= 0 and (year % 400 == 0 or year % 4 == 0 and year % 100 != 0))


def main():
    try:
        year = int(input("Yil: "))
    except ValueError:
        print("Xato. Butun son kiriting.")
    else:
        if kabisa(year):
            print("Kabisa")
        else:
            print("Odatiy yil")
    finally:
        print("The end!")


if __name__ == '__main__':
    main()
