import random


def generation(s):
    # s=level ( user input)
    number = random.randrange(0, s)
    # random generete int between 1 to user input

    number = int(number)

    return number


def main():
    # user input, if it's not integer, promps it again
    while True:
        user_input = input("Level: ")
        try:

            number = int(user_input)  # Try to convert to an integer
            if number > 0:
                break  # Exit the loop if the input is valid
        except ValueError:
            continue

    n = generation(number)
    # print(n)

    while True:
        user_guess = input("Guess:")
        try:
            user_guess = int(user_guess)
            if user_guess < n:
                print("Too small!")
            elif user_guess > n:
                print("Too large!")
            else:
                print("Just right!")
                exit()

        except ValueError:
            continue
    # print()

   # user input to generate random number (function)


main()
