# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    '''

    for char in secret_word:

        if (char in letters_guessed) == False:
            guessed = False
            break
        else:
            guessed = True
    return guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
      which letters in secret_word have been guessed so far.
    returns: string, comprised of letters, underscores (_), and spaces that represents
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    corrct_letters = []

    guess_string = ""
    for item in letters_guessed:
        if item in secret_word:
            corrct_letters.append(item)

    for char in secret_word:
        if char in letters_guessed:
            guess_string += char
        else:
            guess_string += "_ "
    return guess_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase

    unguessed = ""

    for char in letters:
        if char not in letters_guessed:
            unguessed += char
    return unguessed


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining_guess = 8
    remaining_warning = 3

    letters_guessed = []
    duplicate_guess = []

    display = ' _ ' * len(secret_word)

    print('Are You Ready for the Hangman Game?')
    print("I'm holding an English word. Number of letters of this word: " + str(len(secret_word)))

    while True:
        letters_left = get_available_letters(letters_guessed)
        print('Number of remaining rights: ' + str(remaining_guess))
        print('Letters you can use:  ' + letters_left)
        print(display)
        print('Letters you choose: ' + str(letters_guessed))
        print('Copy letters you already selected:' + str(duplicate_guess))
        print('Remaining warning: ', remaining_warning)
        print( 'Number of remaining rights: ',remaining_guess)
        user_guess = (input("Let's guess: ")).lower()

        if remaining_guess == 7:
            print('''
     +---+
         |
         |
         |
        ===''')
        elif remaining_guess == 6:
            print('''
     +---+
     O   |
         |
         |
        ===''')
        elif remaining_guess == 5:
            print('''
 .   +---+
    O   |
    |   |
        |
       ===''')
        elif remaining_guess == 4:
            print('''
    +---+
    O   |
   /|   |
        |
       ===''')
        elif remaining_guess == 3:
            print('''
    +---+
    O   |
   /|\  |
        |
       ===''')
        elif remaining_guess == 2:
            print('''
    +---+
    O   |
   /|\  |
   /    |
       ===''')
        elif remaining_guess == 1:
            print('''
    +---+
    O   |
   /|\  |
   / \  |
       ===''')

        if not user_guess.isalpha():
            if remaining_warning == 1:
                print('Warning count is over!')
                break

            else:
                print('You entered the letter')
                remaining_warning -= 1

        else:

            if user_guess in letters_guessed:

                duplicate_guess.append(user_guess)
                if remaining_warning == 1:
                    print('Warning count is over!')
                    break
                else:
                    print('You entered the same letter!')
                    remaining_warning -= 1

            elif user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                if remaining_guess == 1:
                    print('Your right to guess is over!' + secret_word)
                    break

                else:
                    remaining_guess -= 1

                if user_guess in secret_word:
                    display = get_guessed_word(secret_word, letters_guessed)
                    if is_word_guessed(secret_word, letters_guessed):
                        print("Congratulations! You found the word I'm holding", secret_word)
                        break

                    else:
                        print('Try your luck once more!')



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i].isalpha() and my_word[i] != other_word[i]:
                return False
            elif my_word[i] == "_" and other_word[i] in my_word:
                return False
        return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list.append(word)

    if len(list) != 0:
        print(list)
    else:
        print('No matches found')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    remaining_guess = 15
    remaining_warning = 3

    letters_guessed = []
    duplicate_guess = []

    display = ' _ ' * len(secret_word)

    print('Are You Ready for the Hangman Game?')
    print("I'm holding an English word. Number of letters of this word: " + str(len(secret_word)))

    while True:
        letters_left = get_available_letters(letters_guessed)
        print('Number of remaining rights: ' + str(remaining_guess))
        print('Letters you can use:  ' + letters_left)
        print(display)
        print('Letters you choose: ' + str(letters_guessed))
        print('Copy letters you already selected:' + str(duplicate_guess))
        print('Remaining warning: ', remaining_warning)
        print('Number of remaining rights: ', remaining_guess)
        print('<------------------------------------------->')
        user_guess = (input("Let's guess: ")).lower()

        if remaining_guess == 7:
            print('''
         +---+
             |
             |
             |
            ===''')
        elif remaining_guess == 6:
            print('''
         +---+
         O   |
             |
             |
            ===''')
        elif remaining_guess == 5:
            print('''
     .   +---+
        O   |
        |   |
            |
           ===''')
        elif remaining_guess == 4:
            print('''
        +---+
        O   |
       /|   |
            |
           ===''')
        elif remaining_guess == 3:
            print('''
        +---+
        O   |
       /|\  |
            |
           ===''')
        elif remaining_guess == 2:
            print('''
        +---+
        O   |
       /|\  |
       /    |
           ===''')
        elif remaining_guess == 1:
            print('''
        +---+
        O   |
       /|\  |
       / \  |
           ===''')

        if user_guess == "*":
            print("Olabilecek Kelimeler:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            remaining_warning += 1

        if not user_guess.isalpha():
            if remaining_warning == 1:
                print('Warning count is over!')
                break

            else:
                print('You entered the letter')
                remaining_warning -= 1

        else:

            if user_guess in letters_guessed:

                duplicate_guess.append(user_guess)
                if remaining_warning == 1:
                    print('Warning count is over!')
                    break
                else:
                    print('You entered the same letter!')
                    remaining_warning -= 1

            elif user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                if remaining_guess == 1:
                    print('Your right to guess is over!    ' + secret_word)
                    break

                else:
                    remaining_guess -= 1

                if user_guess in secret_word:
                    display = get_guessed_word(secret_word, letters_guessed)
                    if is_word_guessed(secret_word, letters_guessed):
                        print("Congratulations! You found the word I'm holding",  secret_word)
                        break

                    else:
                        print('Try your luck once more!')
                        print('------------------------------')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)