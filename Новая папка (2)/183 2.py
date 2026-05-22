lst = ['User1', 'User2', 'user3', 'User4']
# Проверяем, что все элементы списка начинаются с заглавной буквы
result = all(item.istitle() for item in lst)
print(result)