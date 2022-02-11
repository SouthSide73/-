import math
print('Введите значение x:', )
x = int(input())
y = (abs(x) + 2 * math.tan(x)) / (5.78 * pow(math.e, x - 1))
print('Значение y:', y)
