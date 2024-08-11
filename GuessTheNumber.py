'''import random


def display():
    print("Welcome to the number guessing game\n I'm thinking of number between 1 to 100")
    level = input("Choose the difficulty level, Type 'easy' or 'hard : '")
    if level == 'easy':
        return "you have only 10 attempts"
    elif level == 'hard':
        return "you have only 5 attempts"


def user_input():
    x = input("please enter your number")



def number_gernater():
    ran_number = random.randint(1, 100)
#print(display(),number_gernater())
'''
import random
EASY_LEVEL_TURN = 10
HIGH_LEVEL_TURN = 5
answer = random.randint(1,100)
print("Welcome to the number guessing game\n I'm thinking of number between 1 to 100")
guess = int(input("Guess the number: "))
turn = 0
def check_answer(guess,answer):
    if guess >answer:
        return "too high"
    elif guess < answer:
        return "too low"
    else:
        print(f"You got an Answer {answer}")
def set_difficulty():


print("Welcome to the number guessing game\n I'm thinking of number between 1 to 100")
guess = int(input("Guess the number: "))
turn = 0
def set_difficulty():
    level = input("Choose the difficulty level, Type 'easy' or 'hard : '")
    if level == 'easy':
        turn = EASY_LEVEL_TURN
        return "you have only 10 attempts"
    else:
        turn = HIGH_LEVEL_TURN




