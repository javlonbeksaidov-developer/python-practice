
'''
Klonlash (Nusxa olish): Berilgan [10, 20, 30] roʻyxatidan nusxa oling (yangi oʻzgaruvchiga tenglang). 
Yangi roʻyxatning oxiriga 40 sonini qoʻshing va ikkala roʻyxatni ham konsolga chiqarib tekshiring.
'''

old_numbers = [10, 20, 30]

new_numbers = old_numbers[:] # [:] - royhatdan nusxa olish
new_numbers.append(40)

print(old_numbers)
print(new_numbers)