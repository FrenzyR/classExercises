password : str = "passivise"
print("Give me the password kind one")
user_input : str = input()
if user_input.casefold() == password:
    print("Correct!")
else:
    print("Incorrect!")