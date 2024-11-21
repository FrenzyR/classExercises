print("Give me a positive number")
user_input: int = int(input())
for x in range(user_input+1):
    if x != 0:
        print("*"*x)

