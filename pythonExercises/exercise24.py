print("Give me a positive number")
user_input = int(input())
def numberSum(n):
    return n * (n + 1) / 2

for i in range(user_input):
    print(numberSum(i))
