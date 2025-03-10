import validators


def main():
    print(validate(input("Email: ")))


def validate(email):

    #>>> validators.email('someone@example.com')
    # True
    # check if the email is valid
    validation = validators.email(email)
    # print(validation)
    if validation == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
