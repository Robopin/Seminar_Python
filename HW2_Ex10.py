coin_list = ['Орел','Решка', 'Орел', 'Орел', 'Решка']
a = 0
b = 0
for i in range(len(coin_list)):
    if coin_list[i] == 'Решка':
        a+=1
    else:
        b+=1
if a > b: print(b)
esle: print(a)