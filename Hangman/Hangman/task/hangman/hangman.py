import random
import sys

words = ['python', 'java', 'swift', 'javascript']
attempts = 8
won = 0
lost = 0


def menu():
    while True:
        _input = input('Type "play" to play the game, '
                       '"results" to show the scoreboard, '
                       'and "exit" to quit:')
        if _input == 'exit':
            sys.exit()
        if _input == 'results':
            print(f'You won: {won} times.\n'
                  f'You lost: {lost} times.')
        if _input == 'play':
            break


def outcome():
    if output == word:
        print(f'''You guessed the word {word}!
        You survived!''')
        global won
        won += 1
    else:
        print('You lost!')
        global lost
        lost += 1


def output_gen():
    _output = ""
    for j in word:
        if j in guess_set:
            _output += j
        else:
            _output += "-"
    return _output


def check_input():
    while True:
        print("\n" + output)
        _guess = input('Input a letter: ')
        if len(_guess) != 1:
            print('Please, input a single letter.')
            continue
        if _guess.isupper() or not _guess.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
            continue
        if _guess in guess_set:
            print("You've already guessed this letter.")
            continue
        return _guess


print('H A N G M A N')
while True:
    word = random.choice(words)
    guess_set = set()
    output = "-" * len(word)
    menu()
    while attempts:
        guess = check_input()
        guess_set.add(guess)
        if guess in word:
            output = output_gen()
            if output == word:
                break
        else:
            attempts -= 1
            print("That letter doesn't appear in the word.")
    outcome()

