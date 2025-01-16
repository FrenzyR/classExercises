clown : float = 0.112
doll : float = 0.075

def weightShippingCalculator(productOneAmount, productTwoAmount, productOne, productTwo):
    return "The shipping weighs " + str(productOneAmount * productOne + productTwoAmount * productTwo)  + " kilograms"

print(weightShippingCalculator(5, 2, clown, doll))