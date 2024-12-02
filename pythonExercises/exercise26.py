print("Would you be so kind as to give me your weight please(in kilos)?")
user_weight : int = int(input())
print("And your height, please (in meters)?")
user_height : int = int(input())

def bodyMassIndex(weight, height):
    return weight / (height*height)

print("Your BMI is: "+ str(bodyMassIndex(user_weight, user_height)))