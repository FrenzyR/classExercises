print("give me a number and i'll tell you if it's a prime or not")
user_input : int = int(input())
is_prime : bool = True
for x in range(user_input):
    if x > 1:
        if user_input % x == 0:
            is_prime = False

print("So... was it a prime?")
if is_prime:
    print("yeah")
else:
    print("nah")