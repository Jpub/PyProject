"""Dice Roller, by Al Sweigart al@inventwithpython.com
Simulates dice rolls using the Dungeons & Dragons dice roll notation.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, simulation"""

import random, sys

print('''Dice Roller, by Al Sweigart al@inventwithpython.com

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program
''')

while True:  # 메인 프로그램 루프:
    try:
        diceStr = input('> ')  # 주사위 문자열을 입력하기 위한 프롬프트
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 주사위 문자열을 정리한다:
        diceStr = diceStr.lower().replace(' ', '')

        # 입력된 주사위 문자열에서 "d"를 찾는다:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # 주사위의 숫자를 얻는다.(예를 들어, "3d6+1"에서 "3"):
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # 더하기 또는 빼기 기호가 있는지 찾는다:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # 주사위 면의 수를 찾는다.(예를 들어, "3d6+1"에서 "6"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # 조건부의 수를 찾는다.(예를 들어, "3d6+1"에서 "1"):
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                # 조건부의 수를 음수로 바꾼다:
                modAmount = -modAmount

        # 주사위 굴리는 것을 시뮬레이션한다:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # 총합을 표시한다:
        print('Total:', sum(rolls) + modAmount, '(Each die:', end='')

        # 굴린 각각의 주사위를 표시한다:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # 조건부의 수를 표시한다:
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # 예외 사항이 발생하면 사용자에게 메시지를 표시한다:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # 주사위 문자열을 입력하는 프롬프트로 돌아간다.
