"""6. Ro'yxat ichida lug'at (Nested Dictionary)

3 ta mahsulotning ma'lumotlarini (nomi, narxi, brendi) lug'at ko'rinishida yozing va bu 3 ta lug'atni bitta ombor deb nomlangan ro'yxat (list) ichiga joylang. Sikl orqali barcha mahsulotlarning faqat nomini va narxini konsolga chiqaring."""


def main():
    mahsulot_1 = {
        "nomi" : "matiz",
        "narxi" : 45_000,
        "brendi" : "gm",
    }

    mahsulot_2 = {
        "nomi" : "spark",
        "narxi" : 44_000,
        "brendi" : "gm",
    }

    mahsulot_3 = {
        "nomi" : "tico",
        "narxi" : 25_000,
        "brendi" : "gm",
    }

    ombor = [mahsulot_1, mahsulot_2, mahsulot_3]

    for i in ombor:
        print(f"{i["nomi"]} {i["narxi"]}")


if __name__ == "__main__":
    main()
