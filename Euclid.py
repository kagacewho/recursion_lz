a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
def Euclid(a, b):
    if a == 0 or b == 0: 
        return max(a, b)
    else:
        if a > b:
            return Euclid(a - b, b)
        else:
            return Euclid(a, b - a)
print('Число Евклида равно:', Euclid(a, b))
