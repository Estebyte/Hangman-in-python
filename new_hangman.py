import random
import os

def select_word(path):
    # Create a list with the words of 'data.txt' and pick a random word.
    with open(path, "r") as file:
        data = [i.strip() for i in file]
    word = random.choice(data)
    return word

def run():
    # Create the word the user will try to find.
    word = (select_word("data.txt"))

    # Set the numbers of attemps with a simple operation with lenght of the word
    attemps = len(word) + (len(word) // 2)

    # Create an underlines list with the same lenght than the word
    underlines = list("_" * len(word))  

    while True:
        os.system("clear")
        # A dirty game cheat! uncomment to activate.
        #print(word)
        print(underlines)
        letter = input(f"Hangman! Guess the word, you have {attemps} attemps ==> ").lower()

        # Input filter. It will only allow to enter one alphabet letter
        try:
            if not letter.isalpha() or len(letter) != 1:
                raise Exception("Oops, you can only enter one letter...")
        except Exception as error:
            os.system("clear")
            input(f"{error} Press Enter to continue: ")
            continue
            
        # Search letter in word.   
        if letter in word:
            # Change "_" in underlines by letter when the letter is in word.
            for index, values in enumerate(word): 
                if values == letter:
                    underlines[index] = letter
            os.system("clear")
        else:
            # When it's not, take one attemp.
            attemps -=1
            os.system("clear")

        #Win event
        if not "_" in underlines:
            os.system("clear")
            print(underlines)
            print("Great! You won <3")
            break

        #Lose event
        if attemps == 0:
            os.system("clear")
            print(f"Sorry, you lost... The word was: {word}")
            break

if __name__ == "__main__":
    run()
