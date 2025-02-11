import inflect

p = inflect.engine()


def main():
    # mylist = p.join(("apple", "banana", "carrot"), final_sep="")
    list1 = []
    while True:
        try:

            userInput = input("Name:")
            list1.append(userInput)

        except EOFError:
            print()
            mylist = p.join(list1)
            print("Adieu, adieu, to", mylist)
            break


main()
