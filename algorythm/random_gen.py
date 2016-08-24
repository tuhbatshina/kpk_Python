i = 1
number = (i * 693 + 5) % 100
print(number)
min = None
while number !=0:
    if number % 3  == 0:
        if min == None or number < min:
            min = number
    i +=1
    number = (i * 693 + 5) % 100
    print(number)
print(min)
