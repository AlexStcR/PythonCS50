def fuel(x):
    x = x.split("/")
    for i in range(len(x)):
        x[i] = int(x[i])
       # print(i)

    rounded_tank = (x[0]/x[1])
    return rounded_tank


def check2(y):

    if y <= 0.01:
        return "E"
    elif y >= 0.99 and y <= 1:
        return "F"
    elif y > 1:
        return main()

    else:
        y = y
    y = ("{:.0%}".format(y))

    return y


def errors(x):

    try:
        x = (check2(fuel(x)))

    except ValueError:

        return main()

    except ZeroDivisionError:

        return main()

    return x


def main():
    x = (input("Fraction:"))
    print(errors(x))


main()
