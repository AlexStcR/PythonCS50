def main():
    inpt = input( "What time is it?")

    #print(convert(inpt))

    #toth1= convert(inpt)

    if 7<= convert(inpt)<= 8:
        print("breakfast time")
    if 12<= convert(inpt)<= 13:
        print("lunch time")
    if 18<= convert(inpt)<= 19:
        print( "dinner time")








def convert(time):
    hour, minute = time.split(":")
    #print(hour, minute)
    h= int(hour)
    m=int(minute)/60

    toth=h+m
    return toth

    #print(toth)





    #breakfast : 7:00 and 8:00
    #lunch 12:00 and 13:00
    #dinner 18:00 and 19:00




if __name__ == "__main__":
   main()
