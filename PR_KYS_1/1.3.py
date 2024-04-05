from math import cos


def main(y, x, z):
    result = (
        (abs(76*y**2 + z/49 + 92*x**3))**6 +
        (27 + 82*x**2 + y/64)**2 +
        ((cos(1 + x**2 + z**3)/83) + (1 - z - 8*y**2)**3) /
        (6*(y**3 + 1)**3 - (30*z**3 + x**2)**7)
    )
    return result


print(main(-0.96, -0.65, 0.25))