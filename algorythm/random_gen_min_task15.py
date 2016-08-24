def generate_number():
    return lambda random_seed: (random_seed*693 + 5)%100
number = generate_number()
i = 1
while number(i)%3 != 0:
    i += 1
temp_minimum = number(i)
i += 1
while number(i) != 0:
     if number(i)%3 == 0:
         if number(i) < temp_minimum:
             temp_minimum = number(i)
     i += 1
print(temp_minimum)