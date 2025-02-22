s = (
    {1964, 1958, 'DIFF'},
    {1964, 1958, 'APL'},
    {1964, 1970},
    {1964, 1987},
    {2017},
    {1967, 1958, 2009},
    {1967, 1958, 1961},
    {1967, 1970, 'DIFF'},
    {1967, 1970, 'APL'},
    {1967, 1987, 2009},
    {1967, 1987, 1961},
)


def main(r):
    s1 = set(r)
    return [i for i in range(len(s)) if not (len(s[i] - s1))][0]


print(main({2017, 1961, 1987, 'DIFF'}))
print(main({1967, 1961, 1970, 'DIFF'}))
print(main([1967, 2009, 1987, 'APL']))
