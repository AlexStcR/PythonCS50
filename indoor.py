def get_lower():
    lower = input()
    return lower

def main():
    lower = get_lower()
    if lower.islower():
        print  (lower)
    else :
        print ( lower.lower())



main()
