"""Powerball Lottery, by Al Sweigart al@inventwithpython.com
A simulation of the lottery so you can experience the thrill of
losing the lottery without wasting your money.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, humor, simulation"""

import random

print('''Powerball Lottery, by Al Sweigart al@inventwithpython.com

Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.

This simulation gives you the thrill of playing without wasting money.
''')

# 사용자가 1 ~ 69까지의 숫자들 중 첫 5개 숫자를 입력하도록 한다:
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 5 17 23 42 50)')
    response = input('> ')

    # 5개가 입력되었는지 확인한다:
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue

    # 문자열을 정수로 변환한다:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    # 숫자들이 1 ~ 69 사이의 숫자인지 확인한다:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    # 그 숫자가 유일한지 확인한다:
    # (중복을 제거하기 위해 숫자로 세트를 만든다.)
    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue

    break

# 사용자는 1 ~ 26 사이에서 파워볼 숫자를 고른다:
while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')

    # 문자열을 정수로 변환한다:
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue

    # 그 숫자가 1 ~ 26 사이의 수인지 확인한다:
    if not (1 <= powerball <= 26):
        print('The powerball number must be between 1 and 26.')
        continue

    break

# 얼마나 플레이할 것인지 입력한다:
while True:
    print('How many times do you want to play? (Max: 1000000)')
    response = input('> ')

    # 문자열을 정수로 변환한다:
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    # 입력한 숫자가 1 ~ 1000000 사이의 수인지 확인한다:
    if not (1 <= numPlays <= 1000000):
        print('You can play between 1 and 1000000 times.')
        continue

    break

# 시뮬레이션을 실행한다:
price = '$' + str(2 * numPlays)
print('It costs', price, 'to play', numPlays, 'times, but don\'t')
print('worry. I\'m sure you\'ll win it all back.')
input('Press Enter to start...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # 당첨 번호를 구한다:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # 당첨 번호를 표시한다:
    print('The winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')

    # 참고: 세트(Set)는 순서가 없으므로,
    # set(numbers)와 set(winningNumbers)에 있는 숫자들의 순서는 중요하지 않다.
    if (set(numbers) == set(winningNumbers)
        and powerball == winningPowerball):
            print()
            print('You have won the Powerball Lottery! Congratulations,')
            print('you would be a billionaire if this was real!')
            break
    else:
        print(' You lost.')  # 여기에 앞쪽 여백이 필요하다.

print('You have wasted', price)
print('Thanks for playing!')
