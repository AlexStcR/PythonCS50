from pyfiglet import Figlet

import sys
import random
figlet = Figlet()





# ---------------------------------------

def function1():
    s= input("Input:")

    figlet.setFont(font=sys.argv[2])
    return print(figlet.renderText(s))





# --------------------------------------------


def function2():
    s= input("Input:")


    available_fonts = figlet.getFonts()

    random_font = random.choice(available_fonts)
    figlet.setFont(font=random_font)
    return print(figlet.renderText(s))


def main():
    if len(sys.argv) == 1:
        #print("1")
        #inpt = input("Input:")
        function2()
    elif len(sys.argv) == 3:
        available_fonts = figlet.getFonts()
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" :
            if sys.argv[2] in available_fonts:
              function1()
            else:
                print("Invalid usage")
                return sys.exit(1)
        else:
            print("Invalid usage")
            return sys.exit(1)


    # output text in a specific font, in which case the first of the two

    else:
        print("Invalid usage")
        return sys.exit(2)
    # print(sys.argv[1])
    #inpt = input("Input:")
    # print(argv[1])
    #check = argv(inpt)


main()
