def main():
    s=(input())
    print(shorten(s))


def shorten(word):
    #expects a str as input and returns that
    #same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
    word=str(word)
    vowel=["a","e","i","o","u","A","E","I","O","U"]
    for x in word:
        if x in vowel:
            word=word.replace(x,"")
    return word

if __name__ == "__main__":
    main()
