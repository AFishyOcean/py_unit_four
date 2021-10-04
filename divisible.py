def is_divisible(num1, num2):
    ans = num1 % num2
    if ans == 1:
        return False
    else:
        return True

    """
    Checks to see if one number is evenly divisible by the second
    :param num1: The number being tested
    :param num2: The divisor
    :return: True if num1 is evenly divisible by num2, false otherwise
    """



def main():

    # Get the two pieces of input from the user.
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    is_divisible(num1, num2)
    if False:
        print(num1, "is not easily divisible by", num2)
    elif True:
        print(num1, "is divisible by", num2)


if __name__ == '__main__':
    main()
