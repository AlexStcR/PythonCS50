import random


def main():
    lvl = get_level()
    user_guess = print(f"Score:", generate_integer(lvl))


def get_level():
    # prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer
    # returns a randomly
    # generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

    while True:
        try:
            lvl = int(input("Level:"))
            if lvl == 1:
                return 1

            elif lvl == 2:
                return 2
            elif lvl == 3:
                return 3
            else:
                print("Input 1,2 or 3")

        except ValueError:
            print("Input 1,2 or 3")


def generate_integer(level):
    trying = 0
    score = 0

    while trying < 10:
        
        if level == 1:
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
        elif level == 2:
            x = random.randrange(10, 99)
            y = random.randrange(10, 99)
        elif level == 3:
            x = random.randrange(100, 999)
            y = random.randrange(100, 999)
        else:
            raise ValueError

        answer = x+y

        try:

            wrong = 0
            while wrong < 3:
                #
                guess = int(input(f"{x} + {y} = "))
                if answer == guess:
                    trying += 1

                    break
                elif wrong == 2:
                    print("EEE")
                    print(f"{x} + {y} =", answer)
                    score += 1
                    trying += 1
                    break

                else:
                    print("EEE")
                    wrong += 1
                    # score+=1

        except ValueError:
            print("EEE")
            # score+=1

    return trying-score


if __name__ == "__main__":
    main()
