def main():
    inpt= input("Greeting:")
    print(f"${value(inpt)}")


def value(greeting):
    x=greeting
    x=x.lower().strip()
    if "hello" in x:
        return 0
    elif x[0] == "h":
        if x != "hello":
            return 20
        else:
            return 0
    else:
        return 100


if __name__ == "__main__":
    main()
