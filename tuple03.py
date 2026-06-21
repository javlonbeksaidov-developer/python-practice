
'''
Tuple'ni Listga o'tkazish: Berilgan (5, 10, 15) 
o'zgarmas ro'yxatini list() yordamida oddiy ro'yxatga o'tkazing, 
unga 20 sonini qo'shing va yana tuple() qilib qaytarib qo'ying.
'''

tuple_numbers = (5, 10, 15)
list_numbers = list(tuple_numbers)
list_numbers.append(20)
tuple_numbers = tuple(list_numbers)

print(type(tuple_numbers))
print(tuple_numbers)