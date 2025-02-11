def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    if "$" in d:
       newd= d.replace("$"," ")
       doll = float(newd)
       #print(doll)
       return doll


def percent_to_float(p):
    if "%" in p:
        newp= p.replace("%"," ")
        newp1=float(newp)
        perc = newp1/100
        #print(perc)
        return perc



main()
