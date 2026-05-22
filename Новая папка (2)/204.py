def square(x):
 """Возводит число в квадрат."""
 return x ** 2

def cube(x):
 """Возвращает куб числа."""
 return x ** 3

def cube_of_square(x):
 """Выводит на экран куб квадрата числа."""
 square_result = square(x)
 cube_result = cube(square_result)
 print(f"Куб квадрата числа {x} равен {cube_result}")
 return cube_result
print(cube_of_square)