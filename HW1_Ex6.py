num = int(input('Введите число: \n'))
count = 0
summ_R = 0
summ_L = 0
while num > 10:
    if count < 3:
        summ_R += num % 10
        num //= 10
    else:
        summ_L += num % 10
        num //= 10
    count += 1
summ_L += num
if summ_L ==summ_R:
    print('Билет счастливый')
else:
    print('Билет не счастливый')