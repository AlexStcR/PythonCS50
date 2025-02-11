import sys

def main():
    print(text_reader(argv_check()))
def argv_check():
    if len(sys.argv)<2:
        #print("Too few command-line arguments")
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)> 2:
        #print("Too many command-line arguments")
        sys.exit("Too many command-line arguments")

    x=sys.argv[1]
    for i in range(len(x)):
        #print(x)
        if x[-3:] != ".py":
            #print("Not a python File")
            sys.exit("Not a python File")
    return x
def text_reader(x):

    try:
        with open(x,"r") as f:
            contents=f.readlines()
            number_lines=len(contents)
        #print(contents)
        for x in (contents):
            if x.lstrip().startswith("#"):
                number_lines-=1
        for lines in contents:
            if lines.strip()=="":
                number_lines -=1
        #print(number_lines)
    except(FileNotFoundError):
        sys.exit("FileNotFoundError")
    return number_lines


main()






