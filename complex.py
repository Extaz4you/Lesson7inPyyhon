def complexnum(x,y,znak):
    if znak == '*':
        return complex(x) * complex(y)
    if znak == '/':
        return complex(x) / complex(y)
    if znak == '+':
        return complex(x) + complex(y)
    if znak == '-':
        return complex(x) - complex(y)