"""Fibonacci Sequence, by Al Sweigart al@inventwithpython.com
Calculates numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math"""

import sys

print('''Fibonacci Sequence, by Al Sweigart al@inventwithpython.com

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True:  # 메인 프로그램 루프
    while True:  # 사용자가 유효한 입력을 할 때까지 계속 요청한다.
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # 사용자가 유효한 숫자를 입력하면 루프를 빠져 나간다.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # 사용자가 1 또는 2를 입력하면 특별한 경우로 처리한다:
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue

    # 사용자가 너무 큰 수를 입력하면 경고를 출력한다:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    # n번째 피보나치 수를 계산한다:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # 첫 번째 2개의 피보나치 수를 표시한다.

    # 피보나치 수열의 모든 수를 출력한다:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # 수열에 있는 다음 수를 출력한다:
        print(nextNumber, end='')

        # 사용자가 원하는 n번째 수를 찾았는지 검사한다:
        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            break

        # 콤마를 출력하여 수열의 수를 구분한다:
        print(', ', end='')

        # 마지막 두 숫자를 옮긴다:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
