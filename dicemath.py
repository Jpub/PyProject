"""Dice Math, by Al Sweigart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, math"""

import random, time

# 상수 설정하기:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # 하단에 합을 입력할 공간을 위해 3만큼 뺀다.

# 전체 퀴즈 시간은 초 단위이다:
QUIZ_DURATION = 30  # (!) 이것을 10 또는 60으로 바꿔 보자.
MIN_DICE = 2  # (!) 이것을 1 또는 5로 바꿔 보자.
MAX_DICE = 6  # (!) 이것을 14로 바꿔 보자.

# (!) 다른 숫자로 바꿔 보자:
REWARD = 4  # (!) 정답일 때 받게 될 점수
PENALTY = 1  # (!) 오답일 때 빼게 될 점수
# (!) PENALTY를 음수로 설정하여
# 오답일 때 점수를 받도록 하자!

# 주사위가 화면에 맞지 않으면 프로그램은 중단된다:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Al Sweigart al@inventwithpython.com

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# 정답과 오답의 수를 추적한다:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:  # 메인 게임 루프
    # 표시할 주사위를 준비한다:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0]은 주사위 면의 문자열 리스트를 포함한다:
        diceFaces.append(die[0])
        # die[1]은 주사위 면의 눈 개수를 포함한다:
        sumAnswer += die[1]

    # 각 주사위의 좌측 상단 구석의 (x, y) 튜플을 담는다.
    topLeftDiceCorners = []

    # 주사위가 어느 방향으로 갈지 알아낸다:
    for i in range(len(diceFaces)):
        while True:
            # 주사위를 놓을 캔버스의 임의의 위치를 찾는다:
            left = random.randint(0, CANVAS_WIDTH  - 1 - DICE_WIDTH)
            top  = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # 모든 네 모서리에 대한 x, y 좌표를 구한다:
            #      왼쪽
            #      v
            #상단 > +-------+ ^
            #      | O     | |
            #      |   O   | DICE_HEIGHT (5)
            #      |     O | |
            #      +-------+ v
            #      <------->
            #      DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # 이번 주사위가 이전 주사위와 겹치는지 확인한다.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # 이번 주사위의 각 모서리가
                # 이전 주사위의 영역 안에 들어가 있는지 확인한다:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRightX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                            overlaps = True
            if not overlaps:
                # 이것은 겹치지 않았다. 따라서 현 위치에 놓을 수 있다:
                topLeftDiceCorners.append((left, top))
                break

    # 캔버스에 주사위를 그린다:

    # 키는 (x, y) 튜플이며,
    # 값은 캔버스 그 위치의 문자다:
    canvas = {}
    # 각 주사위마다 루프를 돈다:
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        # 주사위 면의 각 문자에 대해 루프를 돈다:
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # 이 문자를 캔버스의 올바른 위치에 복사한다:
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # 문자열 리스트인 dieFace에서는
                # x와 y가 서로 바뀐다는 것을 기억하자:
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # 화면에 캔버스를 표시한다:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # 새로운 줄을 출력한다.

    # 사용자가 답을 입력하게 한다:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

# 최종 스코어를 표시한다:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', score)
