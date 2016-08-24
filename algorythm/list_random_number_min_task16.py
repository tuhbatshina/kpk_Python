my_list = [(lambda x:(x*87 + 12)% 16 )(i) for i in range(20)]
print(my_list)
min = my_list[19]
n = 0
while len(my_list) > 0:
    x = my_list.pop()
    if x < min:
        min = x
        n = 1
    elif x == min:
        n += 1
print('min = ', min, 'n = ',n)