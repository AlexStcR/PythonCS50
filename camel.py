def transform(name):
     x=""


     for i in range(len(name)):
        #print(i, end="")
        #print(name[i])
        if name[i].isupper():
            #st=str(name[i])
            #print(st)
            x=x+"_" +name[i].lower()



           # print(x)

        else:
            x=x+name[i]
           #print(name[i], end="")
           #print(nm)

     return x






def main():

    camel=input("CamelCase:")
    print(transform(camel))

main()
