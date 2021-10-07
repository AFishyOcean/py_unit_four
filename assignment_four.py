import random

def get_type():
    type = input("Enter the symbol for the type of problem you would like:")
    if type == "*":
        return "*"
    elif type == "-":
        return "-"
    elif type == "/":
        return "/"
    else:
        return "+"
def get_max():
    max = input("What would you like for the max range to be")
    return max
def problem(t, m):
    num1 = random.randint(0, m)
    num2 = random.randint(0, m)
    if t == "+":
        ans = num1 + num2
    elif t == "-":
        ans = num1 - num2
    return ans
def main():
    t = get_type()
    m = get_max()
    problem(t, m)


if __name__ == '__main__':
    main()