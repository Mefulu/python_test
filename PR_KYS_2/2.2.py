import math


def main(z):
    return (
        70*z**15 if z < -4 else
        1 - 45*(abs(z))**5 if z < 92 else
        81*math.cos(z)+70*(6-56*z**3)**5+z**3/6
    )


print(main(100))
