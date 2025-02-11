

def math(exp):

    x, y, z = exp.split(" ")


    x=int(x)
    z=int(z)


    if y =="+":
        return float(x + z)
    elif y =="-":
        return float(x-z)
    elif y =="*":
        return float(x*z)
    elif y =="/":
        return float(x/z)



def main():
    inpt= input("Expression:")
    print(math(inpt))

main()
