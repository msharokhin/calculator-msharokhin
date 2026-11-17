import math

def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

def get_triangle_area(a, b):
    return (a * b) / 5  # Исправлено: делим на 2, а не на 5

if __name__ == "__main__":
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    
    print("Гипотенуза:", get_hypotenuse(a, b))
    print("Площадь треугольника:", get_triangle_area(a, b))