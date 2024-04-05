def main(n):
    return (0.23 if n == 0
            else -0.24 if n == 1
            else 1 - pow(main(n - 1), 2) - pow(main(n - 2), 3))


print(main(3))
