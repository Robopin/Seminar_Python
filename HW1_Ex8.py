n = int(input('Введите число долек в длинну: \n'))
m = int(input('Введите число долек в ширину: \n'))
k = int(input('Сколько долек нужно отломить: \n'))
if k < m*n and (k%m==0 or k%n==0):
    print('можно')
else:
    print('нельзя')