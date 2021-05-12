import math
figure = input()
if figure == "square":
    a = float(input())
    s = a * a
    print(f"{s:.3f}")
if figure == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b
    print(f"{s:.3f}")
if figure == "circle":
    r = float(input())
    s = math.pi * math.pow(r, 2)
    print(f"{s:.3f}")
if figure == "triangle":
    a = float(input())
    b = float(input())
    s = (a * b) / 2
    print(f"{s:.3f}")