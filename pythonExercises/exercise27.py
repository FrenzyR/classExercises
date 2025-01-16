def taxCalculator(amount, percentage):
    return amount + (amount * (percentage/100))

def taxCalculatorWithNoTaxGiven(amount):
    return amount + (amount * 0.21)


print("Give me an amount of money you want to calculate the taxed priced of")

moneyInput = int(input())

print(taxCalculatorWithNoTaxGiven(moneyInput))

print("Now do me the favor of giving me the % of tax you want")

taxInput = int(input())

print(taxCalculator(moneyInput,taxInput))
