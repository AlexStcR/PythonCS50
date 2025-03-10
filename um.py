import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r'\b([uU][mM])\b'
    match = re.findall(pattern, s)
    n=int()

    if match:
        for i in range(len(match)):
           # print(i)
            n=n+1
        return n
    else:
        return 0

if __name__ == "__main__":
    main()
