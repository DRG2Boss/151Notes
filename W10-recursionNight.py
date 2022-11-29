# Math reminder: n! = n*(n-1)*(n-2)...
# Older loop option (not being used).
def loop_fact(n):
    result = 1
    for number in range(1, n):
        result = result*number
    return n * result


# New recursion option!
def fact(n):
    # This "if" portion is our base case.
    if n <= 1:
        return 1
    # This "return" portion is our recursive case.
    return n * fact(n-1)


def main():
    my_n = int(input("what number shall we calculate factorial:"))
    result = fact(my_n)
    print(f"the result is {result}")


main()
