import sys
import csv
from PIL import Image,ImageOps

def main():

    x, y = argv_checker()
    image_shirt(x,y)

    #conv_names(x, y)
    #in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input

    #sys.exit
    #if the user does not specify exactly two command-line arguments,
#if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
#if the input’s name does not have the same extension as the output’s name, or
#if the specified input does not exist.

def argv_checker():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    x = sys.argv[1]
    y = sys.argv[2]

    if not x.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Not an Image File")
    if not y.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Not an Image File")

    if not x.endswith(y.split('.')[-1]):
        sys.exit("The extensions do not match.")
    return x,y
def image_shirt(x,y):
    with Image.open(x) as img:
        #print(img.size)
        #print(img.format)
        shirt = Image.open("shirt.png")
        size = shirt.size

        img=ImageOps.fit(img,size)
        img.paste(shirt, shirt)
        img.save(y)

















if __name__ == "__main__":
    main()
