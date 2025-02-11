
def main():
        validcoins= [25,10,5]
        total=50
        while total>0:

            print("Amount Due:",total )
            money=int(input("insert a coin:"))
            if money in validcoins:

                 change=total-money


                 if change==0:
                       print("Change Owed:",change)
                 elif change< 0:
                       print("Change Owed:",((-1)* change))


                 total-=money
                 #print(total)



main()



