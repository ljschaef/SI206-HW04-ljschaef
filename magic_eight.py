import randrange from random


def magic_eight(question):
    if question[len(question) - 1] != '?':
        print("I'm sorry, I only accept questions")
    else:
        rand_answer = randrange(0, 20)
        return rand_answer

