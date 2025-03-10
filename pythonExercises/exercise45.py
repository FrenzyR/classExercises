# Fai unha función que recolla como parámetro unha lista de números e nos indique que elementos son primos

arbitrary_numbers : list = [1, 2, 3, 4, 5, 8, 7, 11, 13, 20, 9]

def which_are_prime(numbers):
    for number in numbers:
        if number != 1:
            is_prime(number)


def is_prime(number):
    result = all(number % i for i in range(2, number))
    if result:
        print(str(number)+" is prime")
    else:
        print(str(number)+" is not a prime")

which_are_prime(arbitrary_numbers)