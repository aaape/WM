import math
def quadratic(a, b, c):
    x = (-b + math.sqrt(b*b - 4 * a * c)) / 2 * a
    return x
    print(quadratic(4, 2, 3))
