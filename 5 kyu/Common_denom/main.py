from fractions import Fraction


def convert_fracts(lst):
    denoms = map(lambda x: Fraction(x[0], x[1]).denominator, lst)
    denom = 1
    for den in denoms:
        denom = denom * Fraction(denom, den).denominator
    for numset in lst:
        numset[0], numset[1] = numset[0] * (denom // numset[1]), denom
    return(lst)