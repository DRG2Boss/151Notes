def is_palindrome(string_to_check):
    # Three major "base cases" for a palindrome.
    if string_to_check == "":
        return True
    if len(string_to_check) == 1:
        return True
    if string_to_check[0] != string_to_check[-1]:
        return False
    # Now our recursive case. Note our callback to slicing from W3.
    return is_palindrome(string_to_check[1:-2])


def main():
    maybe_palindrome = input("What should we check for being a palindrome? ")
    answer = is_palindrome(maybe_palindrome)
    if answer:
        print("That was a Palindrome!")
    else:
        print("Nope!!")


main()
