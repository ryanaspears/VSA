# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don"t need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r", 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
counter = 8
counter2 = 0
word = wordlist[random.randint(1, 55901)]
word_list = list(word)
word_length = int(len(word_list))
blanks = []
while counter2 < word_length:
    blanks.append("_")
    counter2 = counter2 + 1
print "Welcome to the game, Hangman!"
print"I am thinking of a word that is", word_length, "letters long"
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
while counter > 0:
    print"You have", counter, "guesses left."
    print "Available letters: " + "".join(alpha)
    guess = raw_input("Please enter your letter or take a guess at the word: ")
    counter1 = 0
    counter3 = 0
    while counter1 < word_length:
        if guess == word_list[counter1]:
            blanks[counter1] = guess
        elif guess != word_list[1]:
            counter = counter - 1
        counter1 = counter1 + 1
        while counter3 < 26:
            if guess == alpha[counter3]:
                alpha[counter3] = ""
            counter3 = counter3 + 1
    print " ".join(blanks)
