import ratio as rat
import complex as com
choise = int(input('Выберите : 1. Рациональные числа. 2. Комплексные числа  '))
if choise == 1:
    a = int(input('Введите первое число'))
    znak = str(input('Введите знак'))
    b = int(input('Введите второе число'))
    print(rat.rat(a, b, znak))
if choise == 2:
    x = complex(input('Первое комплексное число(без пробелов) '))
    znak = str(input('Введите знак '))
    y = complex(input('Второе комплексное число(без пробелов) '))
    print(com.complexnum(x, y, znak))
else:
    print('Неверное число')