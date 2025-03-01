# Dylan Stitt
# Bagels

import random, time, os

def rules():
    print("""I am thinking of a unique 3-digit number. Try to guess what it is.
The clues I give are...
When I say:    That means:
  Bagels       None of the digits is correct.
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
I have thought up a number. You have 10 guesses to get it.""")

    input('\nPress ENTER to begin the game')
    os.system('cls')

def generateNumber():
    number = ''
    for i in range(3):
        num = random.randint(0, 9)
        while str(num) in number:
            num = random.randint(0, 9)
        number += str(num)
    return number


def userGuess():
    guess = input("Guess a 3 digit number where the numbers are all different: ")

    try:
        int(guess)
        while len(guess) != 3:
            guess = input("Try again: ")
            int(guess)

        if len(set(guess)) != 3:
            print('Those are not unique digits')
            time.sleep(.5)
            os.system('cls')
            return userGuess()

    except:
        print('That was not a number')
        time.sleep(.5)
        os.system('cls')
        return userGuess()

    return guess


def checkWin(guess, number):
    if guess == number:
        return True

    d = {}
    for i in guess: d[i] = None

    for i in range(3):
        if guess[i] == number[i]:
            d[guess[i]] = 'FERMI'
            print(">> FERMI")

    for i in range(3):
        if guess[i] in number and d[guess[i]] is None:
            print('>> PICO')

    if len([i for i in list(d.values()) if i is None]) == 3:
        print('>> BAGELS')

    return False

def playAgain():
    ans = input('\nWould you like to play the game again (y/n): ').lower()
    while ans not in ['y', 'n']:
        ans = input('Would you like to play the game again (y/n): ').lower()

    if ans == 'y':
        os.system('cls')
        main()

def main():
    rules()

    playing = True
    tries = 10
    number = generateNumber()

    while playing and tries > 0:
        guess = userGuess()
        win = checkWin(guess, number)

        if not win:
            tries -= 1
            print(f'That was not correct. You have {tries} tries left\n\n')
        else:
            print(f'\n\nYOU WON! You got it in {10 - tries} tries')
            input('Press ENTER to continue')
            playing = False

    playAgain()

if __name__ == "__main__":
    os.system('cls')
    main()
