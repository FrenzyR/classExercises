# TODO Not entirely sure what the exercise' statement means
print("What's your name friend?")
user_name : str = input()
print("And what's your gender? (M/F)")
user_gender : str = input()
if user_gender == "M".casefold() and user_name.casefold().startswith("n"):
    print("you part of group A")
