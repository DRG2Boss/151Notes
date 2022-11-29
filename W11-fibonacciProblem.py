# Math reminder: Fibonacci of "n", fib(n) = fib(n-1)+fib(n-2)
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)


def main():
    number = int(input("What number shall we use for fibonacci? "))
    result = fib(number)
    print(f"Fibonacci of {number} is {result}.")


main()
