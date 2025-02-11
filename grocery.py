




def main():
    d = {}
    lis = []

    while True:

        try:

            value = input()
            value = value.upper()
            lis.append(value)

            # print(list)
        except EOFError:
            lis = sorted(lis)
            for item in lis:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1
            for x, y in d.items():
                print(y, x)
            return exit()


main()
