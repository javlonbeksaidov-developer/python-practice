

'''
Roʻyxat uzunligi: Foydalanuvchidan oʻzi yaxshi koʻrgan 4 ta taomni soʻrab, roʻyxatga yigʻing. 
Oxirida len() funksiyasi yordamida roʻyxatda nechta taom borligini konsolga chiqaring.
'''

taomlar = []
for i in range(3):
    taom = input(f"{i + 1}-taom: ")
    taomlar.append(taom)
print(taomlar, len(taomlar))
