from fractions import Fraction
def rat(a,b,znak):
    a = Fraction(a)
    b = Fraction(b)
    if znak == '*':
        return a*b
    if znak == '/':
        return a/b
    if znak == '+':
        return a+b
    if znak == '-':
        return a-b