import sys
import requests
import json



def argument():

    if len(sys.argv) < 2:
        print("missing Command-line argument")
        sys.exit(1)

    elif len(sys.argv) == 2:

        try:
            f = float(sys.argv[1])

            return f
        except (ValueError, TypeError):
            print("Command-line argument is not a number!")
            sys.exit(1)


    else:
        print("Input just the amount of bitcoin you want to buy!")
        sys.exit(1)

    return


def bitcoin_price():
    keys = []
    try:
        r = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')



        data = r.json()
        price = data["bpi"]["USD"]["rate_float"]

        price = float(price)
        # print(price)
        return price
    except requests.RequestException:
        print("Error")
        return


def calculus():

    amount = argument()
    price = bitcoin_price()
    # print(price,amount)
    final_price = amount*price

    return final_price


def main():
    

    # g=print(bitcoin_price())
    price = calculus()
    print(f"${price:,.4f}")


main()
