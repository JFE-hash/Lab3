def lucky(num):
    sum1 = []
    sum2 = []
    half = len(num) // 2
    first_half = num[:half]
    for i in first_half:
        sum1.append(int(i))
    second_half = num[half:]
    for i in second_half:
        sum2.append(int(i))
    if sum(sum1) == sum(sum2):
        return 'Билет счастливый'
    else:
        return 'Билет не счастливый('


print(lucky(input()))

# ИЛИ
#
# print((lambda x: sum([int(i) for i in x[:len(x)//2]]) == sum([int (i) for i in x[len(x)//2:]]))(input()))