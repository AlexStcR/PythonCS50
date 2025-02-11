def convert(string) :
        if ":)" or ":(" in string:
            return string.replace(":)", "🙂").replace(":(" , "🙁")




def main():

    nstring = input()
    newstring=convert(nstring)
    print(newstring)




main()


