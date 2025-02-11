def energy(x):
    m = x
    c=300000000
    E = m*c*c
    return E


def main ():

    mass= int(input())
    calculation = energy(mass)
    print( calculation)
main ()

