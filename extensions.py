#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
def file(x):
    x=x.lower().strip()
    if ".gif" in x:
        return "image/gif"
    elif ".jpg"in x:
        return "image/jpeg"
    elif ".jpeg" in x:
        return "image/jpeg"
    elif ".png" in x:
        return "image/png"
    elif ".pdf" in x:
        return "application/pdf"
    elif ".txt" in x:
        return "text/plain"
    elif ".zip" in x:
        return "application/zip"
    else:
        return "application/octet-stream"

def main ():
    inpt= input ("File name: ")
    print(file(inpt))
main()
