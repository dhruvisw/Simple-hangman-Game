# 1855 DHRUVI SWADIA FYDS
import random
#list hang that contains the display of a hangman
hang = [""" 
H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():#list of words to be used under function getRandomWord()
    words = ['rakshita', 'aditee', 'prathamesh', 'kedar', 'sandesh', 'aishani', 'jitendra', 'samreen', 'junaid', 'om', 'aman', 'riya', 'vishal', 'yash', 'rohit', 'shreya', 'akash', 'shubham', 'aditi', 'vinod', 'anurag','bhavesh', 'aakanksha','sanchita', 'pratisha', 'jagdish', 'sanket', 'dhruv', 'shruti', 'aditya', 'roshan', 'ravi', 'gaurav', 'shikha','mahak', 'kundansingh', 'sowmen', 'aradhana', 'saptshree', 'samriddhi', 'akhilesh', 'sanjana', 'dhruvi', 'roma', 'vinay', 'vibha', 'pratyush', 'mirthula', 'parth', 'pankaj', 'ruchi', 'sakshi']

    word = random.choice(words)#random.choice is inbuilt method that returns a randomly selected element from the specified sequence.
    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])#hang-list for the display of hangman missedLetters-already used letters  correctLetters-letters that are in the word secretWord-'_'
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')#conditions for already guessed leeters and only letters allowed
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():# if and only if the user types y the game is repeated otherwise exits from the game.
    return input("\nDo you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The student is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break