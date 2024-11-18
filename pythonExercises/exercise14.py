print("How old are you?")
user_age : int = int(input())
print("And how much do you make monthly?")
user_wage : int = int(input())
if user_age > 16 and user_wage >= 1000:
    print("you gotta pay some taxes bro")
else:
    print("you don't gotta pay some taxes bro")