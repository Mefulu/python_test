def main(n):
    if n == 0:
        return 0.23
    elif n == 1:
        return -0.24
    else:
        return 1 - main(n - 1)**2 - main(n - 2)**3


print(main(3))
