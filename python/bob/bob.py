def response(hey_bob):
    hey_bob = r""+hey_bob
    response = "Whatever."
    if hey_bob.isupper() and hey_bob.endswith('?'):
        response = "Calm down, I know what I'm doing!"
    elif hey_bob.strip().endswith("?"):
        response = "Sure."
    elif hey_bob.isupper():
        response = "Whoa, chill out!"
    elif hey_bob == "" or hey_bob.isspace():
        response = "Fine. Be that way!"
    return response

if __name__ == '__main__':
    print(response("Does this cryogenic chamber make me look fat?"))
    print(response("You are, what, like 15?"))
    print(response("4?"))
    print(response(":) ?"))
    print(response(""))
    print(response("         "))
    print(response("\t\t\t\t\t\t\t\t\t\t"))
    print(response("Okay if like my  spacebar  quite a bit?   "))
    print(response("\n\r \t"))
    print(response("This is a statement ending with whitespace      "))
    print(response("\nDoes this cryogenic chamber make me look fat?\nNo."))