print("Give me a positive number")
user_input : int = int(input())
new_list : str = ""

for x in range(user_input):
    if x % 2 != 0 and x != user_input:
        new_list += str(x) + ","
    elif x % 2 != 0 and x == user_input:
        new_list += str(x)
if new_list.endswith(","):
    new_list = new_list[:-1]
    
print(new_list)
