def magic_eight_ball():
    response = input("What is your question?")
    return response

def check_question():
    response = magic_eight_ball()
    if response[len(response) - 1] != '?':
        print("I'm sorry, I can only accept questions")
        return 1
    elif response == "quit":
        return 0

def __main__():
    stuff = check_question()
    while stuff != 0:
        check_question()
        pass
    print("Thanks for playing!")
    pass
