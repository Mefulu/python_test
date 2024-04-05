import math


def main(z, y):
    sum0 = 0
    for i in range(1, len(z) + 1):
        sum0 += 42 * ((1 + 6 * y[len(z) - math.ceil(i / 3)]
                       + z[len(z) - math.ceil(i / 3)] ** 2) ** 4)
    return 43 * sum0


print(main([-0.53, 0.7, -0.18], [-0.82, 0.11, -0.17]))
