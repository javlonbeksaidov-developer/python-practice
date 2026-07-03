"""2. Talaba baholari (Sikl bilan ishlash)
5 ta talaba va ularning imtihon baholaridan iborat lug'at yarating. for sikli yordamida barcha talabalarning ismini va bahosini chiroyli ko'rinishda konsolga chiqaring (Masalan: "Ali — 85 ball")."""


def bahola(talabalar):
    print("\nTalabalarga ball qo'yish")
    baholanganlar = {}
    for talaba in talabalar:
        ball = int(input(f"{talaba.title()} talaba uchun ball:\n>>> "))
        baholanganlar[talaba] = ball

    print("\nBaholangan talabalar")
    for key, value in baholanganlar.items():
        print(f"{key.title()} - {value} ball")


def main():
    print("Talabalaringizni ismlarini kiriting:")
    talabalar = []
    n = 1
    for i in range(5):
        ism = input(f"{n}-talabaning ismi: ")
        talabalar.append(ism)
        n += 1

    bahola(talabalar)


main()
