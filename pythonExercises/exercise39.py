# Escribir un programa que cre un dicionario simulando unha cesta da compra. O programa debe preguntar o artigo e o
# seu prezo e engadir o par ao dicionario, ata que o usuario decida terminar. Despois débese mostrar por pantalla a lista da compra e o custo total, co seguinte formato
# Lista da compra
# Artigo 1     Prezo
# Artigo 2     Prezo
# Artigo 3     Prezo
# …     …
# Total     Custo
# TODO La parte del formato     
groceries : dict = {}

userProduct = ""
while userProduct != "exit":

    userProduct = input("What's the product? Say exit to exit")
    if userProduct not in groceries and userProduct != "exit":
        userPrice = float(input("What's the price? "))
        groceries.update({userProduct: userPrice})

print(groceries)
