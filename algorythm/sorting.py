
def sort_test(my_sort):
    import random
    A = [1, 2, 3, 4, 5, 6]
    A_ans = [1, 2, 3, 4, 5, 6]
    my_sort(A)
    print('test case #1:' + ('OK' if A == A_ans else "Fail"))

    A = [-1, -2, -3, -4, -5, -6]
    A_ans = [-6, -5, -4, -3, -2, -1]
    my_sort(A)
    print('test case #2:' + ('OK' if A == A_ans else "Fail"))

    A = [-1, 2, -3, 4, -5, 6]
    A_ans = [-5, -3, -1, 2, 4, 6]
    my_sort(A)
    print('test case #3:' + ('OK' if A == A_ans else "Fail"))

    A = [1000]
    A_ans = [1000]
    my_sort(A)
    print('test case #4:' + ('OK' if A == A_ans else "Fail"))

    A = []
    A_ans = []
    my_sort(A)
    print('test case #5:' + ('OK' if A == A_ans else "Fail"))

    A = [random.randint(1, 100) for i in range(1000)]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #6:' + ('OK' if A == A_ans else "Fail"))

    A = [5] * 100
    A_ans = [5] * 100
    my_sort(A)
    print('test case #7:' + ('OK' if A == A_ans else "Fail"))

    A = [ [2], [1], [3],[5], [4], [5]]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #8:' + ('OK' if A == A_ans else "Fail"))


def do_nothing(A):
    pass

def bubble_sort(A):
    N = len(A)
    for prohod in range(1, N):
        for i in range(N-prohod):
            if A[i] > A[i +1]:
                tmp = A[i]
                A[i] = A[i+1]
                A[i+1] = tmp

def choice_sort(A):
    N = len(A)
    for pos in range(0, N - 1):
        for i in range(pos +1, N):
            if A[i]< A[pos]:
                A[pos], A[i] = A[i], A[pos]

def insert_sort(A): #сортировка вставками
    N = len(A)
    for pos in range(1, N):
        i = 0
        while A[i]< A[pos]:
            i +=1
        #уверены, что i указывает на элемент >= вставляемого
        tmp = A[pos]
        for k in range(pos-1, i-1):
            A[k+1] = A[k]
        A[i] = tmp

if __name__ == '__main__':
    print('test bubble_sort:')
    sort_test(bubble_sort)
    print('test choise_sort:')
    sort_test(choice_sort)
    print('test insert_sort:')
    sort_test(insert_sort)
