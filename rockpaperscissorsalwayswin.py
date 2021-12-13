"""Rock,Paper, Scissors (Always Win version)
By Al Sweigart al@inventwithpython.com
The classic hand game of luck, except you always win.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, game, humor"""

import time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# 이 변수는 승리 횟수를 추적한다.
wins = 0

while True:  # 메인 게임 루프
    while True:  # 플레이어가 R, P, S, 또는 Q를 입력할 때까지 계속 요청한다.
        print('{} Wins, 0 Losses, 0 Ties'.format(wins))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # 플레이어가 선택한 것을 표시한다:
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # 극적인 일시 중지와 함께 3까지 카운트를 센다:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # 컴퓨터가 선택한 것을 표시한다:
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins = wins + 1
