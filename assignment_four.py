import random
def get_type():
    """
    asks for the type of problem the person wants to do then returns the reply
    :return:
    """
    type = input("Enter the symbol for the type of problem you would like:")
    if type == "*":
        return "*"
    elif type == "-":
        return "-"
    else:
        return "+"
def get_max():
    """
    gets the highest number that the person wants
    :return:
    """
    max = int(input("What would you like for the max range to be"))
    return max
def genNum(m):
    """
    generates random number with the max
    :param m: highest possible number
    :return: returns a number between 0 and the max
    """
    num = random.randint(0, m)
    return num
def problem(t, num1, num2):
    """
    plugs generated numbers into certain equations based on the asked type of problem
    asks user what the answer to indicated problem
    gives a response if the answer is right or wrong
    :param t:
    :param m:
    :return:
    """
    if t == "+":
        ans = num1 + num2
        print(num1, "+", num2)
    elif t == "-":
        ans = num1 - num2
        print(num1, "-", num2)
    elif t == "*":
        ans = num1 * num2
        print(num1, "*", num2)
    userAns = int(input("Answer ="))

    if userAns == ans:
        print("Correct")
    else:
        print("Sorry that is incorrect.The actual answer is", ans)



def main():
    """
    calls all the functions and assigns variables to them
    :return:
    """
    t = get_type()
    m = get_max()
    num1 = genNum(m)
    num2 = genNum(m)
    problem(t, num1, num2)



if __name__ == '__main__':
    main()