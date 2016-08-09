N = int(input())
# считываем в очередь первые 6 чисел
Q = [int(input()) for i in range(6)]
min_even = 1001 #минимальное четное - начальное значение
beta = 1000001
for i in range(N-6):
    # первый элемент покидает очередь - и соревнуется с текущими минимальными
    x = Q[0]
    min_x = min(_x, x)
    if x%2 == 0 and x < min_even:
        min_even = x
    x = int(input())
    beta = min(x * min_even, beta)
    if x%2 ==0:
        beta = min(beta, x * min_x)
    for i in range(5):
        Q[i] = Q[i + 1]
    Q[5] = x
    #Можно было так (без цикла):
    #Q.pop(0)
    #Q.append(x)
