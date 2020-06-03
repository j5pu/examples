#!/usr/local/bin/python3.7
from collections import namedtuple
'https://www.jetbrains.com/help/pycharm/product-refactoring-tutorial.html#8cd66377'

class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom

        factor = gcd(denom, num)

        return super().__new__(cls, num // factor, denom // factor)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)


def gcd(denom, num):
    x = abs(num)
    y = abs(denom)
    while x:
        x, y = y % x, x
    return y