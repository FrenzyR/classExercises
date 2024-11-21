print("Give me a positive number")
user_input: int = int(input())
new_list: list[str] = ["",]

for x in range(user_input+1):
        new_list.append(x) 

newer_list = new_list[::-1]
print(newer_list[:-1])
