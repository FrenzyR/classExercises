# Similar a exercicios anteriores, podes copiar o feito nesa parte e continuar ampliando:
# Escribir un programa que lea un  enteiro positivo,  n, introducido polo usuario e  despois  mostre en pantalla a suma de todos vos  enteiros desde 1 ata  n.
# Para  facelo implementa  unha función que reciba un valor  n e calcule ou resultado usando a  seguinte formula:
# resultado =  n * ( n +1)  / 2
#
# Xera os test unitarios para a función feita. Chequea por exemplo, algun número do que sepas a solución, que
# ocorre cando lle pasas un número negativo... corrixe a partires do resultado do test o necesario para que saia todo ben.

def increment_until_number(number):
    if number < 0:
        number = number * -1
    result = number * (number + 1) // 2
    return result


def testing_my_function():
    assert increment_until_number(5) == 15
    assert increment_until_number(-5) == 15
    min
