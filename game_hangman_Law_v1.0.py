from time import sleep

# declare variable
goal = "secret"  # correct answer
turns = 5  # chance
guesses = ""  # history of guess

def check_guess():
    turns_new = turns
    for char in goal:
        if char in guesses:
            print(char, end=' ')  # express right word as word
        else:
            print("_", end=' ')  # express wrong word as '_'
    turns_new -= 1  # deduct chances
    return turns_new

user = input("\nWhat is your name?\n")  # request user name
print(f"\nHi~ {user}!")  # welcome
sleep(0.5)
print("\nWhat a minute.\nStart Loading...")
sleep(2)
print("\nTime to play Hangman game!")  # welcome
sleep(1)
lens = len(goal)  # give a hint
print(f"\nHere's a hint! The character is {lens} words.")

while True:
    guess = input("Guess a character!\n")  # request guess word
    sleep(0.7)
    guesses += guess
    if guess != goal:  # wrong answer
        if turns > 2:
            turns = check_guess()
            print(f"\n\nYou have {turns} chances.\nTry again.\n")  # notice remain chances
            sleep(0.7)
        elif turns > 1:
            turns = check_guess()
            print(f"\n\nThis is your last chance.\nYou should think more carefully.")  # notice remain chance
            sleep(0.7)
        else:
            print(f"\nNo~~~~\nThe character was '{goal}'.\nSee you next time~ :)")  # fail massage
            break
    else:  # right answer
        print(f"\nCongratulations {user}! You are genius!")  # celebration massage
        break