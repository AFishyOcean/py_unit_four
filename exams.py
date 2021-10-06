
def gets_a_zero(total_classes, class_missed):
    percent_missed = class_missed / total_classes
    if percent_missed >= .25:
        return True
    else:
        return False
def main():
    total_classes = float(input("How many classes have you had total?"))
    class_missed = float(input("How many have you missed?"))

    if gets_a_zero(total_classes, class_missed) == True:
        print("You get a zero on the test")
    else:
        print("You are good to go")
if __name__ == '__main__':
    main()