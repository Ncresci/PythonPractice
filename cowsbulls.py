#Create a program that will play the “cows and bulls” game with the user.
#The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place,
#they have a “cow”. For every digit the user guessed correctly in the
#wrong place is a “bull.” Every time the user makes a guess,
#tell them how many “cows” and “bulls” they have.
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout the game
#and tell the user at the end.
##
##import random
##num = str(random.randint(1000, 9999))
##guess = input('I\'m thinking of a four digit number, what is that number? For every number that is correct you get a cow for every wrong number you get a cow.')
##cow = 0
##bull = 0
##
##while guess != num:
##    if guess[0] == num[0]:
##        cow = cow + 1
##        guess = input('Guess again!' + 'Cow:', cow, 'Bull', bull)
##    elif guess[1] == num[1]:
##        cow = cow + 1
##        guess = input('Guess again!' + 'Cow:', cow, 'Bull', bull)
##    elif guess[2] == num[2]:
##        cow = cow + 1
##        guess = input('Guess again!' + 'Cow:', cow, 'Bull', bull)
##    elif guess[3] == num[3]:
##        cow = cow + 1
##        guess = input('Guess again!' + 'Cow:', cow, 'Bull', bull)
##    else:
##        guess = input('Guess again!' + 'Cow:', cow, 'Bull', bull)
##
##print('You have guessed correctly!')

import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True #gotta play the game
    number = str(random.randint(0,9999)) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")
