<<<<<<< HEAD
import random





=======
def magic_eight_ball():
    response = input("What is your question?")
    return response
>>>>>>> de2d8eee62e85fdc10f601f011f8b3f27649b0e9

answers = ["It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good"
"Very doubtful"]

get_answer = random.choice(answers)
