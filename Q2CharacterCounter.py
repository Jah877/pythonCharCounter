# Jahkim Brown-Roopnarine
# ICS 3UO - A
# December 5, 2021
# This program will take the input of string and count how many times any character appears. It will run a game where an
# idiom may be typed with the characters displayed, and a user has to guess what the classic idiom is.

# This program is based through a navigation within the main menu. From the main menu, users can choose to run the initial
# program which is character counter for any string that they may choose to input. The extension to this program is a simple
# concept, where the same principle for character counting is used, but users are to guess the idiom that is being broken
# into characters. At any point a user may request help, return to the main menu, or quit the program. All modes are replayable,
# as functions are recursive if the user wishes to use the same mode repetitively.

import random # imports random to be used in later functions


# the getInput function is crucial for online documentation, as well as potential user actions for returning to the main menu, or quitting
# the program at any time.
def getInput(prompt, helpString):
    resp = input(prompt)
    if resp == "quit":
        print("\n" + "Thank you for using this character counter " + name + "!")
        quit(0)
    elif resp == "help":
        print(helpString)
        return getInput(prompt, helpString)
    elif resp == "main menu":
        print("Returning to the main menu...\n")
        mainMenu()
    else:
        return resp
########################################################################################################################
# Below function serves as an introduction. It asks their use for a name and returns some general information about how
# the program works.
def getName():
    name = input("Hi there, what is your name: ")
    print("Hello " + name + "!\n"
          "Welcome to the Character Counter!\n"
          "If at any point you would like the program to terminate, type 'quit'.\n"
          "If at any point you require help, please type 'help'.\n"
          "If at any point you would like to return to the main menu, please type 'main menu'.\n")
    return name

# From the main menu, users are presented with four options to view instructions, use the character counter,
# play the idiom guessing game, or to quit the program. The main menu only ever allows the user to input an integer between 1 and 4
# otherwise it will prompt an error code.
def mainMenu():
    print("Welcome to the Main Menu\n"
          "[1] Instructions\n"
          "[2] Character Counter\n"
          "[3] Idiom Guessing Game\n"
          "[4] Exit")
    print("")

    stopper = False
    while not stopper:
        try:
            selection = int(getInput("Enter your selection: ",
                                     "It seems like you're having some trouble. Please type a number from one of the options to enter a selection.\n"
                                     "For instructions for character counter usage type '1', to access the character counter mode type '2',\n"
                                     "to play the idiom guessing game type '3', to exit the program type '4'.\n"))
            if selection not in range(1, 5):  # error handling to make sure number is within choices presented.
                raise ValueError
            break
            stopper = True
        except (ValueError, TypeError): # error handling to ensure that an input is put in
            print("Error detected. Please re-input your selection")
            stopper = False

    if selection == 1:
        getInstructions()
    elif selection == 2:
        countCharacters()
    elif selection == 3:
        getIdiomGuesser()
    elif selection == 4:
        print("Exit has been selected\n"
              "Thank you using this character counter " + name + "!")
        quit(0)
########################################################################################################################
# The function below is a string based function that tells the user the instructions for play. After the user is done reading
# It will return the user to the main menu to reenter their choice.
def getInstructions():
    print("\n"
          "Instructions for use has been selected.\n"
          "This program will run using two modes! In the character counter mode you will input a phrase of your choice\n"
          "and you will be told how many of each character is used in your phrase! In the Idiom Guessing Game you will\n"
          "be shown all characters within a famous idiom, and you will have unlimited guesses to guess the idiom!\n")

    typeAnything = getInput("\nHope that all makes sense! Type enter to dismiss this message and return to the main menu!", "It seems like you're having some toruble, type enter to dismiss this message.")

    while typeAnything == typeAnything:
        mainMenu()
########################################################################################################################
# The below function is a character counter. It takes the input of any given string that a user may input and counts how
# many of each character are within each string by using a loop to test for characters and add them to the dictionary.
# Afterwards it prints out the details of the dictionary, and displays the characters neatly.
def countCharacters():
    charCountD = {} # sets dictionary for character count to empty.

    print("\nCharacter Counter Selected")
    myString = getInput("Write a phrase that you would like the characters counted for: ", "It seems like you are little bit stuck. Write a phrase that you would like the characters counted for") # takes input for a string
    myString = myString.lower() # makes everything in the string lowercase, so that the counter will not be case sensitive.

    for char in myString: # for every character in the users string
        if char in charCountD: # if a character is in the library
            charCountD[char] += 1 # then that character is a selected key, and a count of 1 is added to it in the library for every time that character appears
        else:
            charCountD[char] = 1 # if it is not already in the library, the a value of one is given to the key, for the first time that it appears. Now every other time it appears, it will qualify for the first if statement.
                                 # at the end of this loop the library has each character as a key and value for how many times it appears as value to the key

    print("\nThe count for all characters in" + " '" + myString + "' " "is: ") # print statement telling the user the count for characters will be

    for item in charCountD: # for every item in the library, which are all the characters
        print(item + ": " + str(charCountD[item]) ) # this will print the character, then a colon, then the string for the number of times that the occurence of the character appears
                                                    # this is found as item is used as a key, and its corresponding value in the dictionary from the prior for loop is string casted

    flag = False
    while not flag: # try and except loop for handling errors while asking the user to play again
                    # gives options to type yes, main menu, quit, or help
        try:
            countAgain = getInput("\nWould you like to count characters for another phrase? (yes/main menu/quit/help) ", "It seems like you are little bit stuck. Type 'yes' to repeat the process for another phrase, 'main menu' to return to the main menu, or 'quit' to quit.")
            if countAgain.upper() != "YES": # if yes isn't type, or the keywords from getInput then value error is raised and user must reinput choice
                raise ValueError
        except(ValueError):
            print("Please enter a valid entry.")

        if countAgain.upper() == "YES": # only valid option, does not worry for any case sensitivity
            flag = True

    countCharacters() # if the loop is escaped, and user not returned to main menu, then the function calls itself and runs the string counter again.
########################################################################################################################
# Helper function, uses same logic as earlier function. Passed a value instead of already defined in mystring like previous.
def helperCounter(phrase):
    dictionary = {}

    for char in phrase:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary
########################################################################################################################
# Simple idiom guesser game. A library is created with numbers as keys, and strings as values. The strings within the dictionary
# are all classic idioms that are in lower case. These classic idioms are shuffled between and then selected to be passed through
# the helper function. The user will then be displayed all the character counts and will have to guess the phrase. The user is told if
# they are right or wrong. If they give up, they can type give up. Then they are prompted to play again.

def getIdiomGuesser():
   idiomsDict = {0: "it's a piece of cake", 1: "it's raining cats and dogs", 2: "kill two birds with one stone", 3: "let the cat out of the bag",
                 4: "break a leg", 5: "easy does it", 6: "bite the bullet"} # dictionary for idioms
   randomIdiomKey = random.randint(0,len(idiomsDict)-1) # random key selected, a random integer is selected within the range of the length of the dictionary.

   selectedIdiomDict = helperCounter(idiomsDict[randomIdiomKey]) # new dictionary created for character counters for random key, for passing a string of a random idiom to the helperCounter
   keyList = list(selectedIdiomDict.keys()) # list of keys within the selectedIdiomDict are made into a list - this a list of all keys and values or (characters and occurences)
   random.shuffle(keyList) # this shuffles all the characters so the idiom is randomly displayed for characters and isn't obvious

   print("\nIdiom Guessing Game mode selected.\n")
   print("You have an unlimited amount of guesses. Below are all the characters included within the idiom. If you\n"
         "ever wish to give up, type 'give up'") # informs the user of game rules

   correct = False
   while not correct: # loop for redisplaying characters counted until they give up guess correctly
       print("\n")
       for char in keyList: # formats dictionary, printing characters and values for characters, using each character as a key in the dictionary
           print("(" + char + ": " + str(selectedIdiomDict[char]) + ")",end=" ")
       guess = getInput("\nWhat do you think the idiom is (with punctuation included!): ", "it seems like you're a bit stuck. Type in a guess for what you think the idiom might be.") # user makes guess

       if guess.lower() == idiomsDict[randomIdiomKey]: # lowercases everything, if user is right, loop stops and they win
           correct = True
           print("You have guessed the idiom correctly. You win! ")
       elif guess.lower() != idiomsDict[randomIdiomKey] and guess.lower() != "give up": # if user is wrong and they haven't given up loop runs another iteration
           print("You have guessed incorrectly. Try again")
       elif guess.lower() == "give up": # if they give up, loop ends
           correct = True
           print("You have left the game!")

   flag = False # asks them to play again, same logic as prior
   while not flag:
       try:
           countAgain = getInput("Would you like to play again (yes/main menu/quit/help)? ",
                                  "It seems like you are little bit stuck. Type 'yes' to play agin, 'main menu' to return to the main menu, or 'quit' to quit.")
           if countAgain.upper() != "YES":
               raise ValueError
       except(ValueError):
           print("Please enter a valid entry.")

       if countAgain.upper() == "YES":
           flag = True

   getIdiomGuesser()
########################################################################################################################
name = getName() # introduction function
mainMenu() # runs through main menu