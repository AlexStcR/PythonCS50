def date_numbers(x):
    # transform  to yy-mm-dd

    x = x.split("/")
    day = int(x[1])
    mm = int(x[0])
    year = int(x[2])
    if mm < 0 or mm > 13:
        return
    if day < 0 or day > 32:
        return
    else:
        return f"{year}-{mm:02d}-{day:02d}"

    # newx=f'{year}-{month:02}-{day:02}'
    # print('{}-{}-{}'.format(year , month, day))

    # return f'{year}-{month:02}-{day:02}'


def date_letters(y):
    # y=y.replace(",", " ")
    y = y.replace(",", " ").strip()

    y = y.split()

    # print(y)
    for i in range(len(y)):
        if y[i] in month:
            # ('{}-{}-{}'.format(y[2], y[1], month.index(y[i])))
           # print(month.index(y[i]))
            month1 = int(month.index(y[i]))
           # print(month1 +1 )
            yy = y[2]
            dd = int(y[1])
            mm = month1+1
            if dd < 0 or dd > 32:
                return
            else:
                continue

            # print(f'{yy}-{mm:02}-{dd}')

        # else:
            # print(y[i])
           # print (y)
            # print(f'{yy}-{mm:02}-{dd}')
            # return True
        # else:
            # return "invalid"
    return f"{yy}-{mm:02d}-{dd:02d}"


def checking(date):

    try:
        if "," in date:
            date = date.capitalize()
            # date_letters(date)

            return date_letters(date)
        elif "/" in date:

            return date_numbers(date)
        else:
            return

    except (ValueError, IndexError, TypeError, UnboundLocalError):
        return


    # return date
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]


def main():
    while True:

        inpt = input("Date:")
        # stop=checking(inpt)
        result = checking(inpt)
        print(result)
        # print(months(inpt))
        # print(months(inpt))

        if result == None:
            return main()
        else:
            # print("2")
            break


main()
