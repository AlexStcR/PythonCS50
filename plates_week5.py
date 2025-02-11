def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    #vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    #“No periods, spaces, or punctuation marks are allowed.”
    #any letters in the user’s input will be uppercase
    #is_valid returns True if s meets all requirements and False if it does not
    #Assume that s will be a str


    for z in range(len(s)):
       #print(len(s))
       #g=int(len(s)/2)
       #print(g)
       #print(s[x])
       if s[0:2].isalpha()and s.isupper() and s.isalnum()and len(s)>1 and len(s)<7:
           #print(1)
           validation= True
       else:
           #print(2)
           return  False


    for x in range(len(s)):
                    if s[x].isdigit():
                       #print (2)
                       if s[x:].isdigit():
                           #print(s[len(s)-1])
                           validation=True

                       else:
                           return False
    for g in range(len(s)):
                        if s[g]=='0':
                        #print(len(s)-1)
                            #print(4)
                        #print(s[len(s)-1])
                            if s[len(s)-1]=='0':
                                #print("iha!")
                                validation= True
                            else:
                                return False




                          #print(s[x])
                          #print([x])

    return validation


if __name__ == "__main__":
      main()








