"""9. Login va Parol tizimi (Avtorizatsiya)

users = {'admin': '12345', 'javlon': 'p@ssword', 'user1': 'qwerty'} lug'ati berilgan. Foydalanuvchidan login va parol so'rang.

Agar login xato bo'lsa: "Bunday foydalanuvchi mavjud emas"

Agar login to'g'ri, lekin parol xato bo'lsa: "Parol noto'g'ri"

Ikkalasi ham to'g'ri bo'lsa: "Tizimga xush kelibsiz!" degan xabarlar chiqsin."""

def main():
    users = {
        'rol' : 'admin',
        'login' : 'javlon',
        'parol' : '1234', 
    }

    login = input("Login: ")
    parol = input("Parol: ")

    if login != users['login']:
        print("Bunday foydalanuvchi mavjud emas")
    else:
        if parol != users['parol']:
            print("Parol noto'g'ri")
        else:
            print("Tizimga xush kelibsiz!")


if __name__ == "__main__":
    main()