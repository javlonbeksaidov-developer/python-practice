"""1-mashq: Boshlang'ich (String va Ro'yxat bilan ishlash)
Topshiriq: Matnni teskari aylantiruvchi va uning faqat unli harflarini sanovchi funksiyalar yozing hamda ularni testlang.
Funksiya 1: teskari_matn(text: str) -> str
Funksiya 2: unlilar_soni(text: str) -> int (Unlilar: a, e, i, o, u)
Kutilayotgan testlar:
Oddiy matn berilganda to'g'ri ishlashi.
Bo'sh matn "" berilganda 0 yoki "" qaytarishi.
Katta-kichik harflar (case-insensitivity) hisobga olinishi.
"""


def reverse(text):
    return text[::-1]


def count_vowel(text):
    vowels_count = 0
    for harf in text:
        if harf in "aeuioAEUIO":
            vowels_count += 1
    return vowels_count


def main():
    while True:
        print("\n1. reverse\n2. count vowel\n0. exit")
        choose = input(">>> ")
        if choose == "0":
            break
        elif choose == "1":
            text = input("Text kiriting:\n>>> ")
            print(reverse(text))
        elif choose == "2":
            text = input("Text kiriting:\n>>> ")
            print(count_vowel(text))
        else:
            print("Takror")


if __name__ == "__main__":
    main()
