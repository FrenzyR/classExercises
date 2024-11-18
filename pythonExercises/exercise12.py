print("Give me a number hotshot")
first_number : int = int(input())
print("Give me another number")
second_number : int = int(input())

def user_division(n1, n2):
    if n2 == 0:
        return "you can't do that sir"
    return n1/n2

print(user_division(first_number, second_number))