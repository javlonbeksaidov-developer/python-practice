"""10. Murakkab lug'at strukturasi (E-Katalog)

Quyidagi strukturaga ega lug'at yarating va foydalanuvchidan qaysi brendning telefonini ko'rmoqchi ekanligini so'rang (masalan: "Apple"). Agar o'sha brend mavjud bo'lsa, uning ichidagi modellarni va narxlarini chiqarib bering.

Python
smartphones = {
    "Apple": {
        "iPhone 14": 900,
        "iPhone 15 Pro": 1200
    },
    "Samsung": {
        "Galaxy S23": 850,
        "Galaxy A54": 400
    }
}"""


def main():
    smartphones = {
        "apple": {"iPhone 14": 900, "iPhone 15 Pro": 1200},
        "samsung": {"Galaxy S23": 850, "Galaxy A54": 400},
    }

    brend = input("Brend (apple, samsung):\n>>> ").strip().lower()

    if brend in smartphones:
        for key, value in smartphones[brend].items():
            print(f"Modeli: {key} - narxi: {value}")


if __name__ == "__main__":
    main()
