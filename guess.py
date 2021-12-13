"""Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, game"""

import random


def askForGuess():
    while True:
        guess = input('> ')  # 예상하는 값을 입력한다.

        if guess.isdecimal():
            return int(guess)  # 문자열을 숫자로 변환한다.
        print('Please enter a number between 1 and 100.')


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
secretNumber = random.randint(1, 100)  # 무작위 숫자를 선택한다.
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # 플레이어에게 10번의 기회가 주어진다.
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break  # 숫자를 맞췄다면 for 루프에서 빠져나온다.

    # 힌트를 제공한다:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# 결과를 공개한다:
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secretNumber)
