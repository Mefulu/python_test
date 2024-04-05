import math


def main(z):
    if z < -4:
        return 70*z**15
    elif -4 <= z < 92:
        return 1-45*(abs(z))**5
    elif z >= 92:
        return 81*math.cos(z)+70*(6-56*z**3)**5+z**3/6


print(main(100))
