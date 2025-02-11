
def fortytwo(x):
    x =x.lower().replace("-"," ").strip()

    if (x == "42" or x == "forty two"):
        return "Yes"

    else :
        return "No"

def main():
    inpt= input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    print(fortytwo(inpt))


main()


