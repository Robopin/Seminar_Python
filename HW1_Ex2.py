num = int(input('Введите число: \n'))
summ = 0
while num > 10:
    summ += num % 10
    num //= 10
summ += num
print (summ)

