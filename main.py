#functions for generating random numbers
import random

#generates random integer from 1-50 and stores in a variable num.
num = random.randint(1, 50)

#variable tries to count how many attempts the player makes
tries = 0

#print instructions on the screen
print("Guess my number (1-50)!")

#starts infinite loop
while True:
    # try block is to handle potential error if error occurs it will jump to except block
    try:
        # prompts user with > gets input text from user int used to convert text to int and stores in variable g
        g = int(input("> "))
        # add +1 to tries count
        tries += 1
        # checks is the guess is higher
        if g < num: print("Higher!")
        # checks is the guess is lower
        elif g > num: print("Lower!")
        # runs only if the guess == random number
        else:
            # prints successfully message
            print(f"Right! It took {tries} tries.")
            # exit while loop player guessed correct number
            break
    # finds any error in the try block if user enters text
    except: print("Numbers only!")

#functions for generating random numbers
import random

#Creates a list called words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

#Creates a variable score o to track how many words the player got it right
score = 0

#Displays game title on screen
print("WORD SCRAMBLE GAME")

#starts a for loop to loop through each element in words list
for word in words:

    #random.sample(word, len(word)) takes each word and creates random sample of words and shuffling, .join helps to join the shuffled letters into single str
    scrambled = ''.join(random.sample(word, len(word)))

    #displays the scrambled words \n gives blank line before starting
    print(f"\nUnscramble this: {scrambled}")

    #creats inner loop giving player two attempts to each word
    for i in range(2):  # 2 attempts

        #"Guess: " and waits for player to type something .lower() converts the letter to lowercase

        guess = input("Guess: ").lower()

        #checks if the player guessed correct
        if guess == word:

            #displays correct and adds 1 to the score
            print("Correct!")
            score += 1

            #breaks the inner loop
            break

        #if wrong on first attempt
        elif i == 0:

            #prints wrong message
            print("Wrong, try again!")

        #if wrong on second attempt
        else:

            #the inner loop ends shows the correct word
            print(f"Word was: {word}")

#after all words are done shows final score
print(f"\nYour score: {score}/{len(words)}")