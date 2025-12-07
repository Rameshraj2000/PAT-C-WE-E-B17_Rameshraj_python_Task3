# #functions for generating random numbers
# import random
# #generates random integer from 1-50 and stores in a variable num.
# num = random.randint(1, 50)
# #variable tries to count how many attempts the player makes
# tries = 0
#
# #print instructions on the screen
# print("Guess my number (1-50)!")
#
# #starts infinite loop
# while True:
#     try:  #try block is to handle potential error if error occurs it will jump to except block
#         g = int(input("> "))  #prompts user with > gets input text from user int used to convert text to int and stores in variable g
#         tries += 1 #add +1 to tries count
#         if g < num: print("Higher!") #checks is the guess is lower
#         elif g > num: print("Lower!") #checks is the guess is higher
#         else:    #runs only if the guess == random number
#             print(f"Right! It took {tries} tries.") #prints successfully message
#             break  #exit while loop player guessed correct number
#     except: print("Numbers only!") # finds any error in the try block if user enters text
import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
score = 0

print("WORD SCRAMBLE GAME")

for word in words:
    scrambled = ''.join(random.sample(word, len(word)))

    print(f"\nUnscramble this: {scrambled}")

    for i in range(2):  # 2 attempts
        guess = input("Guess: ").lower()

        if guess == word:
            print("Correct!")
            score += 1
            break
        elif i == 0:
            print("Wrong, try again!")
        else:
            print(f"Word was: {word}")

print(f"\nYour score: {score}/{len(words)}")