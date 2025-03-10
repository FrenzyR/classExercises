arbitrary_numbers : list = [2, 4, 5, 8, 7, 11, 13, 20, 9]
more_arbitrary_numbers : list = [2, 4, 34, 8, 20, 12]

def which_are_pairs(numbers):
    for number in numbers:
        if number != 1:
            if not is_pair(number):
                return

    print("They're all pairs")


def is_pair(number):
    if number % 2 == 0:
        return True
    else:
        print(str(number) + " is NOT pair")
        return False

which_are_pairs(arbitrary_numbers)
which_are_pairs(more_arbitrary_numbers)