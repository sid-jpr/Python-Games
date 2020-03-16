"""The Hangman Game"""
# random word is picked & player needs to guess the word
# before hangman is completely drawn

from random import randint
from hangs import HANGMAN_PICS

def main():
    gameEnd = False

    while gameEnd == False:
        playGame()

        # ask if user would like to play again
        while True:
            decision = input('Play Again? (Y / N): ').lower()
            if decision == 'y':
                break
            if decision == 'n':
                gameEnd = True
                break

def playGame():
    secretWord = pick_word()
    guessedLetters = ['_'] * len(secretWord)
    wrongLetters = ''

    print('\n' * 2 + 'H A N G M A N')

    while True:
        print('\n' + 'Secret Word: ' + ' '.join(guessedLetters).capitalize())
        print('Wrong Letters: ' + ' '.join(wrongLetters))
        print(HANGMAN_PICS[len(wrongLetters)])

        # check winning or losing status
        if ''.join(guessedLetters).isalpha():
            print('You Won! :)')
            break
        if len(wrongLetters) >= len(HANGMAN_PICS) - 1:
            print('You Lost! :( | Word was "{}"'.format(secretWord.title()))
            break

        inputLetter = getLetter()

        # check if user guessed the letter
        if inputLetter in secretWord:
            for charNum in range(len(secretWord)):
                if inputLetter == secretWord[charNum]:
                    # Add letter to guessed letters
                    guessedLetters[charNum] = inputLetter
        # check if user already typed this letter
        elif inputLetter in wrongLetters:
            print('You have already typed this letter!')
        # else add to wrong letters
        else:
            wrongLetters = wrongLetters + inputLetter

def getLetter():
    '''
    Gets letter from user as input and validates if the input
    is actually a letter.
    '''

    while True:
        letter = input('Guess a Letter: ')
        if len(letter) == 1 and letter.isalpha() == True:
            return letter.lower()

def pick_word():
    '''
    Creates a list of words with minimum three letters from file.
    Picks and returns random word from the list.
    '''

    filePath = 'words.txt'
    file = open(filePath, 'r')
    words = []

    # add words with min three characters
    for line in file:
        line = line.rstrip('\n')
        if len(line) >= 3:
            words.append(line.lower())

    file.close()

    # draw random word from the list
    word = words[randint(0, len(words))]
    return word

if __name__ == '__main__':
    main()