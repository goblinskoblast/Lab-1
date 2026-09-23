import math


def read_number(prompt: str) -> float:
    return float(input(prompt).replace(",", "."))


a = read_number("Введите сторону a: ")
b = read_number("Введите сторону b: ")
c = read_number("Введите сторону c: ")

if a <= 0 or b <= 0 or c <= 0:
    print("Ошибка: длины сторон должны быть положительными.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Ошибка: из этих сторон нельзя составить треугольник.")
else:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {area:.2f}")
