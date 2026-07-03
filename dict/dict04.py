"""4. Ro'yxatdan lug'atga (Convert)

Ikkita bir xil uzunlikdagi ro'yxat berilgan: kalitlar = ['ism', 'yosh', 'kasb'] va qiymatlar = ['Anvar', 25, 'Dasturchi']. Ushbu ro'yxatlardan foydalanib, yangi lug'at hosil qiling. (Maslahat: zip() funksiyasi yoki range() yordamida sikldan foydalaning)."""


def main():
    kalitlar = ["ism", "yosh", "kasb"]
    qiymatlar = ["Anvar", 25, "Dasturchi"]

    # zip() va dict()
    info = dict(zip(kalitlar, qiymatlar))
    print(info)

    # zip() va for loop
    info = {}
    for key, value in zip(kalitlar, qiymatlar):
        info[key] = value
    
    print(info)


if __name__ == "__main__":
    main()
