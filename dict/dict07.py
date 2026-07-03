'''7. Eng qimmat mahsulot (Mantiq va hisob-kitob)

Mahsulotlar va ularning narxlari lug'ati berilgan. Lug'at ichidagi eng qimmat mahsulotning nomi va narxini aniqlab, konsolga chiqaruvchi kod yozing.'''

def main():
    mahsulotlar = {
        "olma" : 18_000,
        "anor" : 25_000,
        "uzum" : 15_000,
        "behi" : 10_000,
    }

    qimmat = 0
    ism = ""
    for key, value in mahsulotlar.items():
        if value > qimmat:
            qimmat = value
            ism = key
    
    print(f"Eng qimmat meva {ism} va uning narxi: {qimmat}.")


if __name__ == "__main__":
    main()