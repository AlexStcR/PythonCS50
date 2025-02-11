#implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
def greeting(x):
    x=x.lower().strip()
    if "hello" in x:
        return "$0"
    elif x[0] == "h":
        if greeting != "hello":
            return "$20"
        else:
            return "$0"
    else:
        return "$100"


def main ():
    inpt= input("Greeting:")
    print(greeting(inpt))


main()

