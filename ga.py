import math
 
print('введите координаты точки А')
 x1 = float(input())
 y1 = float(input())
print('введите координаты точки В')
 x2 = float(input())
 y2 = float(input())
d=math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
print("Ответ задачи")
print(d)