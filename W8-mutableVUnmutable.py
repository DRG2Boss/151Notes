def param_mess(number, list):
    number = number+3
    list.append(number)
    # Functions with a return statement will stuff the result into the "param_mess(number, list)" function.
    return number*number


def main():
    demo1 = [2, 3, 5]
    demo2 = 3
    result = param_mess(number=demo2, list=demo1)
    print(f"demo2: {demo2}")
    print(f"result {result}")
    print(f"demo1 {demo1}")


main()
