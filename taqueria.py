prices_taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}


def main():

    total = 0
    while True:
        try:

            while True:
                k = input("Item:")
                k = k.title()

                if k in prices_taqueria.keys():
                    prices_taqueria[k] = float(prices_taqueria[k])
                    # print(prices_taqueria[k])
                    # prices_taqueria[k]+=prices_taqueria[k]
                    # print(prices_taqueria[k])
                    total = total + prices_taqueria[k]
                    # total=  "%.2f" % total
                    print(f"Total:${total:.2f}")

                else:
                    return main()

        except EOFError:

            return exit()


main()
