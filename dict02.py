
'''
Qiymatni olish: Yuqoridagi lugʻatdan foydalanib, 
faqat ismingizni konsolga ikki xil usulda chiqarib koʻring: 
bittasi toʻrtburchak qavs ['ism'] bilan, ikkinchisi .get('ism') metodi bilan.
'''

info = {
    "ism" : "Javlon",
    "yosh" : 21,
    "shahar" : "Samarqand"
}

print(info['ism'])
print(info.get('ism'))