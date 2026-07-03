"""1. Mevalar do'koni (Element tekshirish)
Mevalar nomi va ularning narxi yozilgan lug'at tuzing (kamida 4 ta). Foydalanuvchidan meva nomini so'rang. Agar u meva lug'atda bo'lsa, narxini chiqaring, agar bo'lmasa "Bizda bunday meva yo'q" degan xabarni ko'rsating. (Maslahat: in operatoridan yoki .get()dan foydalaning)."""

mevalar = {
    "olma": 12_000,
    "banan": 15_000,
    "uzum": 20_000,
    "shaftoli": 18_000,
    "anor": 25_000,
}


def show_price(meva):
    '''in operatori'''
    # if meva in mevalar:
    #     return f"{meva}ning narxi: {mevalar[meva]}"
    # return "Bizda bunday meva yo'q"

    '''.get() metodi'''
    # result = mevalar.get(meva, "Bizda bunday meva yo'q")
    # return result

    '''1 qator if operatori'''
    # return f"{meva}ning narxi: {mevalar[meva]}" if meva in mevalar else "Bizda bunday meva yo'q"


def main():
    meva = input("Meva: ").strip().lower()
    print(show_price(meva))

main()
