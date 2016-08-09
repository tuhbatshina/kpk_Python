N = 4
#Поиск максимального четного числа
m1 = None
for i in range(N):
    x = int(input())
    if x%2 == 0:
        if  m1 == None or x>m1:
            m1 = x

if m1 == None:
    print('четных чисел нет')
else:
    print('максимальное четное ', m1)