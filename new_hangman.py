import random
import os

def select_word(path):
    with open(path, "r") as file:
        data = [i.strip() for i in file]
    word = random.choice(data)
    return word

def run():
    word = (select_word("data.txt"))
    attemps = len(word) + (len(word) // 2)
    underlines = list("_" * len(word))  

    while True:
        os.system("clear")
        print(word)
        print(underlines)
        letter = input(f"Hangman! Guess the word, you have {attemps} attemps ==>").lower()

        try:
            if letter.isalpha() == False or len(letter) != 1:
                raise Exception("Oops, you can only enter one letter...")
        except Exception as error:
            os.system("clear")
            input(f"{error} Press Enter to continue: ")
            continue
            
        #Search letter in word    
        if letter in word:
            for index, values in enumerate(word): #Change "_" in underlines by letter
                if values == letter:
                    underlines[index] = letter
            os.system("clear")
        else:
            attemps -=1
            os.system("clear")

        #Win event
        if not "_" in underlines:
            os.system("clear")
            print(underlines)
            print("Great! You won")
            break

        #Lose event
        if attemps == 0:
            os.system("clear")
            print(f"Sorry, you lost. The word was: {word}")
            break

if __name__ == "__main__":
    run()
