def terms(n, max_num=None):
    if max_num is None:
        max_num = n
    if n == 0: # возвращаем список с пустым списком
        return [[]]
    if n < 0:  # возвращаем пустой список
        return []
    
    result = []    
    for i in range(1, max_num + 1):  # Рекурсивно вызываем функцию
        for p in terms(n - i, i):
            result.append([i] + p) # Добавляем текущее число к каждому разбиению и добавляем результат в список
    return result  # Возвращаем список всех разбиений
n = int(input('Введите число:'))
partitions = terms(n)
for p in partitions: 
    print('Разложение числа равно:' , p)

    



    




