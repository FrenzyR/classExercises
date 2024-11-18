def suma(x, y):
    return x + y

if __name__ == "__main__":
    print("Dame un numero")
    x = int(input())
    print("Dame otro numero")
    y = int(input())
    result = suma(x, y)
    print(f"El resultado es {result}")