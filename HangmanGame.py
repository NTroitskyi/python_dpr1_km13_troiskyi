# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()
secret_word = choose_word(wordlist)
secret_word_list = list(secret_word)

def is_word_guessed(secret_word, letters_guessed): 
    if list(secret_word) == letters_guessed:
      return True
    else:
      return False

guessed_letters = []

def get_guessed_word(secret_word, letters_guessed):
    b = list('_'*len(secret_word))
    for x in range(len(secret_word)):
        for y in range(len(letters_guessed)):
            if secret_word[x] == letters_guessed[y]:
                del b[x]
                b.insert(x, letters_guessed[y])
    global a            #to use in future
    a = ' '.join(b)     #to make the string with spaces from b
    return a



def get_available_letters(letters_guessed):
    avletters = list('abcdefghijklmnopqrstuvwxyz')
    for x in letters_guessed:
      for y in avletters:
        if x == y:
          del avletters[avletters.index(y)]
        else:
          pass
    return ''.join(avletters)
    
    

def hangman(secret_word):
    print('Welcome to the hangman game.')
    print('Hmmm.... This word consist of', len(secret_word), 'letters') 
    #print(secret_word)          #delete # if you want to see the word before the game and test programme
    guessed_letters = []
    tries_global = 6
    tries_local = 3
    used_letters = []
    avletters = list('abcdefghijklmnopqrstuvwxyz')        #available letters*
    while tries_global > 0:
        print(get_guessed_word(secret_word, used_letters))
        if tries_local == 0:
            tries_global -= 1
            print("You're punised. Tries remains: ",tries_global)     #punising for missing 3 times in a row
            tries_local = 3
            continue
        inputed_letter = input('Enter a letter: ').lower()
        if inputed_letter.isalpha == False:                        #warning1
            tries_local -= 1
            print("It's not a letter. Warnings remains: ",tries_local)
            continue
        elif inputed_letter not in avletters:                   #warning2
            tries_local -= 1
            print('Enter a letter from english alphabet. Warnings remains: ',tries_local)
            continue
        elif len(inputed_letter) > 1:                         #warning3
            tries_local -= 1
            print('Enter only one letter. Warnings remains: ',tries_local)
            continue
        elif inputed_letter in used_letters:                #warning4
            tries_local -= 1
            print("You've already used this letter. Warnings remains: ",tries_local)
            continue
        else:
            tries_local = 3
            used_letters.append(inputed_letter) #adding letters to another list to exclude them from available letters
            print("Available letters: ", get_available_letters(used_letters))
            if inputed_letter in secret_word_list:
                guessed_letters.append(inputed_letter)        #adding to guessed_letters list to know which letters were guessed and prevent repeatings(warning)
            else:
                tries_global -= 1
                print('WRONG! Attempts remains: ', tries_global)
                continue
        print(guessed_letters)
        if is_word_guessed(secret_word, guessed_letters) == True:
            print('The secret word: ', secret_word)
            return "Unfortunately... You won"
    if tries_global == 0:
        print('The secret word: ', secret_word)
        return "You lost, hahahahaha!!!!"







def match_with_gaps(my_word, other_word):
    my_word_normal = str(my_word).replace(" ","")
    length = len(my_word_normal)
    letters_my_word = list(my_word_normal)
    if len(other_word) == length:
        for i in range(length):                                                              
            if my_word_normal[i] == other_word[i]:
               continue
            elif  my_word_normal[i] == "_" and other_word[i] not in letters_my_word:
               continue
            else:
               return False
        return True
    else:
        return False
    




def show_possible_matches(my_word):
    hints = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True :
            hints.append(other_word)
    return hints


def hangman_with_hints(secret_word):         #similar with def hangman() but with hints
    print('Welcome to the hangman with hints game.')
    print('Hmmm.... This word consist of', len(secret_word), 'letters')
    #print(secret_word)             #delete # if you want to see the word before the game and test programme
    guessed_letters = []
    tries_global = 6
    tries_local = 3
    used_letters = []
    avletters = list('abcdefghijklmnopqrstuvwxyz')
    while tries_global > 0:
        print(get_guessed_word(secret_word, used_letters))
        if tries_local == 0:
            tries_global -= 1
            print("You're punised. Tries remains: ",tries_global)
            tries_local = 3
            continue
        inputed_letter = input('Enter a letter. To get hint enter *: ').lower()
        if inputed_letter == '*':
            print(show_possible_matches(a))
            continue
        if inputed_letter.isalpha == False:
            tries_local -= 1
            print("It's not a letter. Warnings remains: ",tries_local)
            continue
        elif inputed_letter not in avletters:
            tries_local -= 1
            print('Enter a letter from english alphabet. Warnings remains: ',tries_local)
            continue
        elif len(inputed_letter) > 1:
            tries_local -= 1
            print('Enter only one letter. Warnings remains: ',tries_local)
            continue
        elif inputed_letter in used_letters:
            tries_local -= 1
            print("You've already used this letter. Warnings remains: ",tries_local)
            continue
        else:
            tries_local = 3
            used_letters.append(inputed_letter)
            print("Available letters: ", get_available_letters(used_letters))
            if inputed_letter in secret_word_list:
                guessed_letters.append(inputed_letter)
            else:
                tries_global -= 1
                print('WRONG! Attempts remains: ', tries_global)
                continue
        if is_word_guessed(secret_word, guessed_letters) == True:
            print('The secret word: ', secret_word)
            return "Unfortunately... You won"
    if tries_global == 0:
        print('The secret word: ', secret_word)
        return "You lost, hahahahaha!!!!"




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

   
    #print(hangman(secret_word))             #delete # if you want to test the game without hints
                                             #and
    print(hangman_with_hints(secret_word))   #print # before if you want to test it without hints
    pass

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
