lst = ['12', '13', '14', '15']
# Проверяем, что каждый элемент начинается на '1'
result = all(item.startswith('1') for item in lst)
print(result)