def dev(n):
    try:
        n = int(n)
    except ValueError:
        return 'Ошибка! Не верный тип данных'
    if n == 0:
        return 'Ошибка! Деление на 0'
    else:
        return 100 / n


print(dev(input()))