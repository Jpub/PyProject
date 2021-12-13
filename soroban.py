"""Soroban Japanese Abacus, by Al Sweigart al@inventwithpython.com
A simulation of a Japanese abacus calculator tool.
More info at: https://en.wikipedia.org/wiki/Soroban
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, math, simulation"""

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - The Japanese Abacus')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    abacusNumber = 0  # 이것은 주판에 표시된 숫자다.

    while True:  # 메인 프로그램 루프
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            # 프로그램 종료하기:
            break
        elif commands.isdecimal():
            # 주판 숫자 설정하기:
            abacusNumber = int(commands)
        else:
            # 증감 명령어 처리하기:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # 주판은 음수를 표시할 수 없다:
        if abacusNumber < 0:
            abacusNumber = 0  # 모든 음수는 0으로 바꾼다.
        # 주판은 9999999999보다 더 큰 숫자를 보여 줄 수 없다:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    hasBead = []  # 각 구슬 위치에 대한 True/False를 담는다.

    # 윗알은 0, 1, 2, 3, 4에 대해 구슬을 위로 올린다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    # 윗알은 5, 6, 7, 8, 9에 대해 구슬을 아래로 내린다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    # 가장 위에 있는 첫 번째 아래알 줄은 0이 아니면 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '12346789')

    # 두 번째 아래알 줄은 2, 3, 4, 7, 8, 9일 때 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    # 세 번째 아래알 줄은 0, 3, 4, 5, 8, 9일 때 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    # 네 번째 아래알 줄은 0, 1, 2, 4, 5, 6, 9일 때 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    # 다섯 번째 아래알 줄은 0, 1, 2, 5, 6, 7일 때 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    # 여섯 번째 아래알 줄은 0, 1, 2, 3, 5, 6, 7, 8일 때 구슬을 갖는다.
    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    # True/False 값을 O/| 문자로 변환하기
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # O 그리고 | 문자로 주판을 그린다.
    chars = abacusChar + numberList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()
