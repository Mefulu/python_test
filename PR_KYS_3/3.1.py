def main(a, m, b):
    sum0 = 0
    for k in range(1, b + 1):
        sum1 = 0
        for i in range(1, m + 1):
            sum2 = 0
            for c in range(1, a + 1):
                sum2 += ((((c - 50 * c**2)**4) / 86) - 75 *
                         (k**2 - 25 * i - 67)**5)
            sum1 += sum2
        sum0 += sum1
    return sum0


print(main(7, 6, 4))
