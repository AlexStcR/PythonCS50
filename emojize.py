import emoji

def emojix(x):
    return emoji.emojize(x,language='alias')




def main():
    inpt=input("Input:")
    print("Output:",emojix(inpt))


main()
