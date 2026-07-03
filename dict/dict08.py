'''8. So'zlar hisoblagichi (Word Counter)

Foydalanuvchidan biror matn (gap) kiritishini so'rang. Matndagi har bir so'z necha marta takrorlanganini hisoblab, natijani lug'at ko'rinishida chiqaring.
Masalan: "olma pishdi olma tushdi" -> {'olma': 2, 'pishdi': 1, 'tushdi': 1}'''

def main():
    text = input("Matn: ")

    word_count = {}
    for soz in text.split():
        if soz in word_count:
            word_count[soz] += 1
        else:
            word_count[soz] = 1
    
    print(word_count)


if __name__ == "__main__":
    main()