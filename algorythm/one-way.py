N = 4
m1_found = False
for i in range(N):
    x = int(input())
    if not m1_found or x>m1:
        m1 = x
        m1_found = True
print(m1)
4
7
2
1

