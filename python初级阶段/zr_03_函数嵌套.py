def test1():
    print("%" * 50)


def test2(char, times):
    print(char * times)
    test1()


def print_lines():
    row = 0
    while row <= 6:
        test2("$", 50)
        row += 1


print_lines()
