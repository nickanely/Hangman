from random import randint # Do not delete this line

def displayIntro():
    print("_______________________________________________")
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")
    print("_______________________________________________")
    print("_____________________Rules_____________________")
    print("Try to guess the hidden word one letter at a   ")
    print("time. The number of dashes are equivalent to ")
    print("the number of letters in the word. If a player ")
    print("suggests a letter that occurs in the word,    ")
    print("blank places containing this character will be ")
    print("filled with that letter. If the word does not  ")
    print("contain the suggested letter, one new element  ")
    print("of a hangman’s gallow is painted. As the game  ")
    print("progresses, a segment of a victim is added for ")
    print("every suggested letter not in the word. Goal is")
    print("to guess the word before the man hangs!  ")
    print("_______________________________________________")


def displayEnd(result):
    if result == True:
        print("________________________________________________________________________")
        print("          _                                  _                          ")
        print("         (_)                                (_)                         ")
        print("__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    ")
        print("\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   ")
        print(" \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      ")
        print("  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      ")
        print("           | |   (_)    | |                  | (_)                      ")
        print("        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ ")
        print("       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|")
        print("      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   ")
        print("       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   ")
        print("________________________________________________________________________")
    else:
        print(" __     __           _           _   _                                    ")
        print(" \ \   / /          | |         | | | |                                   ")
        print("  \ \_/ /__  _   _  | | ___  ___| |_| |                                   ")
        print("   \   / _ \| | | | | |/ _ \/ __| __| |                                   ")
        print("    | | (_) | |_| | | | (_) \__ \ |_|_|                                   ")
        print("    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   ")
        print("        _______ _                                        _ _          _ _ ")
        print("       |__   __| |                                      | (_)        | | |")
        print("          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |")
        print("          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |")
        print("          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|")
        print("          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)")
        print("__________________________________________________________________________")


def displayHangman(state):
    if state == 5:
        print("     ._______.   ")
        print("     |/          ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")


    elif state == 4:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 3:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 2:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |       |   ")
        print("     |       |   ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 1:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |      \|/  ")
        print("     |       |   ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    else:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |      \|/  ")
        print("     |       |   ")
        print("     |      / \  ")
        print("     |           ")
        print(" ____|___        ")


def getWord():
    fileName = "hangman-words.txt"
    file = open(fileName, "r")
    wordList = []
    for x in file.readlines():
        wordList.append(x)
    file.close()
    randomNumb = randint(0, len(wordList) - 1)
    print(wordList[randomNumb])
    return wordList[randomNumb]

def valid(c):
    if len(c) == 1:
        if 122 >= ord(c) >= 97:
            return True
    else:
        return False

def play():
    global hiddenWord
    hiddenWord = getWord()
    listOfHiddenWord = []
    for x in range(len(hiddenWord) - 1):
        listOfHiddenWord.append('_')
    lives = 5
    counter = len(hiddenWord) - 1
    while lives != 0:
        displayHangman(lives)
        print("Guess the word: " + ''.join(listOfHiddenWord))
        print("Enter the letter")
        letter = input("")
        while not valid(letter):
            letter = input("Letter is not valid, please enter again : ")
        numOfGuessedLetters = 0
        for x in range(len(hiddenWord)):
            if hiddenWord[x] == letter:
                if listOfHiddenWord[x] == '_':
                    listOfHiddenWord[x] = letter
                    numOfGuessedLetters += 1
        counter -= numOfGuessedLetters
        if numOfGuessedLetters == 0:
            lives -= 1
        if counter == 0:
            print("Hidden word was: " + hiddenWord)
            return True
    displayHangman(0)
    return False

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        answer = input("Do you want to play again? (yes/no)")
        while answer != "no" and answer != "yes":
            answer = input("Please, enter yes or no: ")
        if answer == "no":
            return
        elif answer == "yes":
            continue

if __name__ == "__main__":
    hangman()

