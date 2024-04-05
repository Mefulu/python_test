#ПРАКТИКА №6 ГРУППА ИКБО-07-22 ВАРИАНТ №31 https://kispython.ru/docs/5/ИКБО-07-22.html#вариант-31
from math import ceil


def main(O):
    N = {abs(o) + 8 * o for o in O if -60 <= o <= 47}
    B = {abs(o) for o in O if o > -77 and o <= 9}
    L = {v - ceil(v / 6) for v in N if (v > -53) ^ (v <= 27)}
    left = len(B | L)
    total = 0
    for b in B:
        for d in L:
            total += b % 3 - 9 * d
    return left - total


print(main({-30, -91, -88, 9, 11, 19, -43, 91, 31, -33}))
print(main({-92, 9, 13, 47, -79, -15, 51, 17, -36}))
