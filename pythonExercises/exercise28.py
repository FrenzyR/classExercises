print("Could  you please give me two numbers?")
numbersTuple : tuple = ()
while len(numbersTuple) != 2:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))


subjects : list = ["math", "chemistry", "french", "i dont know, something?", "html"]

def returnMeAList(first, second, third, fourth, fifth):
    basiclist : list = [first, second, third, fourth, fifth]
    return basiclist

basicList : list = returnMeAList(subjects[0], subjects[1], subjects[2], subjects[3], subjects[4])
print("What did you get in these subjects? : " + str(returnMeAList(subjects[0], subjects[1], subjects[2], subjects[3], subjects[4])))

marksList : list = []
## I am aware this is a poor man's for
i : int = 0
while i <= 4:
    print("Give me your mark in " + str(basicList[i]) + ". ")
    mark = input()
    marksList.append(mark)
    i += 1

def printMeTwoLists(subjectList, markList):
    subjectList : list = subjectList
    markList : list = markList
    listLength : int = len(subjectList)
    y : int = 0
    while y < listLength:
        print("You got " + str(markList[y]) + " on subject " + str(subjectList[y]))
        y += 1

printMeTwoLists(subjects, marksList)

# Escribir un programa que pida ao usuario dous números enteiros e mostre por pantalla a < n> entre < m> dá un  cociente < c> e un resto < r> onde < n> e < m> son os números introducidos polo usuario, e < c> e < r> son o  cociente e o resto da división enteira respectivamente.
#
# Neste exercicio se trata de prácticar o uso de tuplas. Na función que fagas para implementar a división terás como parámetros o dividende o mailo divisor, e vas calcular o dividendo e máis o resto. Como só podes devolver no return un elemento terás que empaquetar a resposta nunha tupla.
#
# No programa principal podes chamar a esa función, recoller o resultado e acceder á tupla devolta para facer a impresión en pantalla.