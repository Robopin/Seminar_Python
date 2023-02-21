# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def rec_st(a, b):
    if b == 1:
        return a
    return (a * rec_st(a,b - 1))
a = int(input("Число: "))
b = int(input("Степень: "))
print("Ответ", rec_st(a, b))