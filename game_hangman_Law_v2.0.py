import csv, random, winsound
from time import sleep

# declare the number of chance and guess bowl
turns = 5  # chance
guesses = ""  # history of guesses

# declare goal and hint
with open('./resource/word_list.csv', 'r') as f:  # read word list
    reader = csv.reader(f)
    next(reader)  # skip header
    words = [i for i in reader]  # change csv to list
random.shuffle(words)  # shuffle words
goal, hint = words[0][0].strip(''), words[0][1]  # declare goal and hint

# method to check guess and goal
def check_guess():
    turns_new = turns
    for char in goal:
        if char in guesses:
            print(char, end=' ')  # express right word as word
        else:
            print("_", end=' ')  # express wrong word as '_'
    turns_new -= 1  # deduct chances
    return turns_new

# start game
user = input("\nWhat is your name?\n")  # request user name
print(f"\nHi~ {user}!")  # welcome
sleep(0.5)
print("\nStart Loading...")
sleep(2)
print("\nTime to play the Hangman game!")  # welcome
sleep(1)
lens = len(goal)  # give a hint
print(f"\nHere's some hints!\n"
      f"First! The character is {lens} words.\n"
      f"Second! The character is {hint}.\n")

while True:
    guess = input("Guess a character!\n")  # request guess word
    sleep(0.7)
    guesses += guess  # add guess to guesses
    if guess != goal:  # wrong answer
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)  # play fail sound
        if turns > 2:
            turns = check_guess()
            print(f"\n\nYou have {turns} chances.\nTry again.\n")  # print remain chances
            sleep(0.7)
        elif turns > 1:
            turns = check_guess()
            print(f"\n\nThis is your last chance.\nYou should think more carefully.")  # print remain chance
            sleep(0.7)
        else:
            print(f"\nNo~~~~\nThe character was '{goal}'.\nSee you next time~ :)")  # fail massage
            break
    else:  # right answer
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)  # play succeed sound
        print(f"\nCongratulations {user}! You are genius!")  # celebration massage
        break