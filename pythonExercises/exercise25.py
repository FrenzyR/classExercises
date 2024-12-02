import math

print("Give me a positive number")

user_input = int(input())

while user_input < 0:
    print("Give me a positive number")
    user_input = int(input())

def turnIntofactorial(n):
    factorial = 1
    for number in range(2, n + 1):
        factorial *= number
    return factorial

print(turnIntofactorial(user_input))
## print(math.factorial(user_input))