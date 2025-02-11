import sys
import csv
from tabulate import tabulate

def main():
    print(reader_csv(argv_check()))

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
        if x[-4:] != ".csv":
            #print("Not a python File")
            sys.exit("Not a CSV File")
    return x
def reader_csv(x):
    try:
        #
        with open ( x, "r") as file:
            reader=csv.DictReader(file)
            table = tabulate(reader,headers = "keys", tablefmt="grid")
            


    except(FileNotFoundError):
        sys.exit("FileNotFoundError")

    return table
main()
