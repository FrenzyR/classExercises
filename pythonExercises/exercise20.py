print("Give me a positive number")
user_input: int = int(input())
new_list: list[int] = [0,]
y : int = 0
for x in range(user_input+1):
        if x != 0:
            print(x+y)
            y=x


