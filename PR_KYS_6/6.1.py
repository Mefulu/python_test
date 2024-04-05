from math import ceil


def main(Y):
    Z = {v % 3 - v // 5 for v in Y if -58 < v <= 72}
    E = {9 * c for c in Z if c < 32 or c > -97}
    P = {3 * v for v in Y if v > -88 or v < 53}
    L = {S * e for S in P for e in E if S >= e}
    left = len(E) + len(L) - len(E & L)
    total = sum(ceil(e / 4) - abs(d) for e in E for d in L)
    return left - total


print(main({-56, -54, -84, 13, -15, 83, 21, 24, -66, 95}))
print(main({98, 37, 42, 12, 77, -80, -3, 89, 58, 61}))
