def main(n):
    arr = [0.23, -0.24]
    for i in range(2, n + 1):
        arr.append(1 - arr[i-1]**2 - arr[i-2]**3)
    return arr[n]


print(main(3))
