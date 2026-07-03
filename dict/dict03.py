"""3. Lug'atni tozalash (Foydalanuvchi tanlovi)

Bir nechta davlatlar va ularning poytaxtlari lug'atini tuzing. Foydalanuvchidan bitta davlat nomini so'rang va o'sha davlatni (kalit va qiymati bilan) lug'atdan o'chirib tashlang. Yakuniy lug'atni konsolga chiqaring."""


def main():
    urta_osiyo_davlatlari = {
        "o'zbekiston": "Toshkent",
        "qozog'iston": "Astana",
        "qirg'iziston": "Bishkek",
        "tojikiston": "Dushanbe",
        "turkmaniston": "Ashxobod",
        "afg'oniston": "Qobul",
    }

    davlat = input("Davlat nomi: ").strip().lower()

    if davlat in urta_osiyo_davlatlari:
        del urta_osiyo_davlatlari[davlat]
        print(urta_osiyo_davlatlari)
    else:
        davlatlar = []
        for key in urta_osiyo_davlatlari.keys():
            davlatlar.append(key.title())

        print(f"Faqat {davlatlar} davlatlar mavjud.")


if __name__ == "__main__":
    main()
