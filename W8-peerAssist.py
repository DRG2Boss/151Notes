
def sayhello():
    print("Hello Class")


def squarenum(num):
    return num*num


def addnums(x, y):
    return x+y


def pet_names(n1, n2, n3):
    print(f"Your pet names are {n1}, {n2}, {n3}. Epic!")


def main():
    sayhello()
    print(squarenum(7))
    z = addnums(10, 25)
    print(z)
    pet_names("Luna", "Dippy", "Doug")


main()
