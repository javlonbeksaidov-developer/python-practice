
'''
Element qoʻshish: Boʻsh roʻyxat oching. 
Unga .append() yordamida ketma-ket 3 ta doʻstingizning ismini qoʻshing 
va roʻyxatni konsolga chiqaring.
'''

dostlar = []

son = int(input("Nechta do'stingiz bor?\n>>> "))
for i in range(son):
    dost = str(input(f"{i+1}-do'stingiz: "))
    dost = dost.title()
    dostlar.append(dost)
print(dostlar)