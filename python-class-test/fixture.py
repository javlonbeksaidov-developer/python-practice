"""4-mashq: Fixture va Obyektlar (@pytest.fixture)
Topshiriq: Onlayn do'kon Savat (Shopping Cart) tizimini test qiling.

Klass: ShoppingCart
add_item(name, price) — mahsulot qo'shadi.
get_total() — umumiy summani qaytaradi.
Kutilayotgan testlar:
@pytest.fixture yaratib, unda 2-3 ta mahsulot qo'shilgan tayyor ShoppingCart obyektini qaytaring.
Ushbu fixture'dan foydalanib, umumiy summa to'g'ri hisoblanayotganini tekshiring.
"""


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = {
            name: price,
        }
        self.items.append(item)

    def show_item(self):
        return self.items

    def get_total(self):
        total = 0
        for box in self.items:
            for i in box.values():
                total += i
        return total


def main():
    savat = ShoppingCart()
    while True:
        print("0. Exit\n1.Add item\n2.Show item\n3.Total")
        choose = input(">>> ")
        if choose == "0":
            break
        elif choose == "1":
            name = input("Mahsulot: ")
            price = int(input(f"{name}ning narxi: "))
            savat.add_item(name, price)
        elif choose == "2":
            print(savat.show_item())
        elif choose == "3":
            print(savat.get_total())

        else:
            pass


if __name__ == "__main__":
    main()
