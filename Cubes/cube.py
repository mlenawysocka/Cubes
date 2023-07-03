import random

suma = 0
number_of_tries = 10000
for j in range(number_of_tries):
    for i in range(3):

        result = random.randrange(1, 7)
        print('Result: ', result)

        if result == 6:
            suma += 1
            break
print(suma)
print('The probability is:', suma / number_of_tries * 100, '%')
