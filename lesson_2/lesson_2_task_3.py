import math

def square(side):
    
    return math.ceil(side * side)

side_length = 6
area = square(side_length)
print("Площадь квадрата = ", side_length, ":", area)