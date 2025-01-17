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