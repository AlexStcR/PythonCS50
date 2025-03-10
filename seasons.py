from datetime import date
import re
import sys
import inflect



# Most comments I've left are for study purposes, so I can remember where I tested with print statements or checked variable types.


def check_format(s):
    pattern = r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
    match = re.search(pattern, s)
    if not match:

        # Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
        sys.exit("Invalid date")
    else:
        # print(s)
        return s


def pass_date(y):
    # print(type(y))

    y = y.split('-')
    list_y = []

    # print(y)
    for i in y:
        list_y.append(int(i))

    return (list_y)


def transform_date(date_):



    year_ = date_[0]
    month_ = date_[1]
    day_ = date_[2]
    Date = date(year_, month_, day_)
    # Accessing the attributes
    tday = date.today()
    # print("today:",Date.today())
    diff = (tday-Date).days
    # print(diff)
    minutes = diff*24*60
    # print(minutes)
    return minutes


def minutes_to_words(m):
    p = inflect.engine()

    # print(m)
    word = p.number_to_words(m, andword="")
    word = word.capitalize()
    # print(word)
    return f"{word} minutes"


def main():


    # creating input
    birth = input("Date of Birth:")

    # starting checking function
    birth_checked = check_format(birth)

    # date object
    x = pass_date(birth_checked)

    # run into the class
    trns = transform_date(x)

    # transform number into words

    time = print(minutes_to_words(trns))


if __name__ == "__main__":
    main()
