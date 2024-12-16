a = (input('Введите первое число:'))
b = (input('Введите второе число:'))

def addition(a, b, perenos=0):

    if not a and not b and perenos == 0:
        return ""

    
    laststroki1 = int(a[-1]) if a else 0
    laststroki2 = int(b[-1]) if b else 0

   
    summa = laststroki1 + laststroki2 + perenos
    perenos = summa // 10
    result_digit = summa % 10

    
    return addition(a[:-1], b[:-1], perenos) + str(result_digit)

print(addition(a, b))



