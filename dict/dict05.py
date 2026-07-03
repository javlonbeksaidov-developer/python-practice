'''5. Lug'at ichida ro'yxat (Nested List)

Biror dasturchining ismi, tillari (ro'yxat ko'rinishida: ['Python', 'JavaScript']) va tajribasi yozilgan lug'at tuzing. Konsolga dasturchining ismini va u biladigan tillarni alohida-alohida (for sikli yordamida) qator qilib chiqaring.'''

def main():
    dev = {
        "name" : "Javlon",
        "lang" : [
            "python",
            "java",
            "c++",
            "kotlin"
        ]
    }

    print(f"Dasturchining ismi {dev['name'].title()}. Quyidagi tillarni biladi:")
    for til in dev["lang"]:
        print(til, end=" ")


if __name__ == "__main__":
    main()