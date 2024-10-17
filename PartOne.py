variable = input("Please enter a variable in camel case.")

def main():
    word = ""
    for alphabet in variable:
        if alphabet.isupper():
            word += "".join("_" + alphabet.lower())
                     
        else:
            word += "".join(alphabet)
    print(word)
main()