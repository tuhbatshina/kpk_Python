#Определить факториал числа x
k = int(input())
factor = 1
for x in range(1,k + 1):
    factor *= x
    print(factor)