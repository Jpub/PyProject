"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, simulation"""

import copy, random, sys, time

# 상수 설정:
WIDTH = 79   # 셀 그리드의 폭
HEIGHT = 20  # 셀 그리드의 높이

# (!) ALIVE의 값을 '#'이나 다른 문자로 바꿔 보자:
ALIVE = 'O'  # 살아 있는 셀을 나타내는 문자
# (!) DEAD의 값을 '.'이나 다른 문자로 바꿔 보자:
DEAD = ' '   # 죽어 있는 셀을 나타내는 문자

# (!) ALIVE를 '|'로 DEAD를 '-'로 바꿔 보자.

# cells와 nextCells는 상태에 대한 값을 가지고 있는 딕셔너리다.
# 키는 (x, y) 튜플이며,
# 값은 ALIVE 또는 DEAD 값 중 하나다.
nextCells = {}
# nextCells에 DEAD와 ALIVE를 무작위로 넣는다:
for x in range(WIDTH):  # 모든 행에 대해 루프를 돈다.
    for y in range(HEIGHT):  # 모든 열에 대해 루프를 돈다.
        # DEAD나 ALIVE가 될 확률은 50퍼센트다.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE  # ALIVE를 추가한다.
        else:
            nextCells[(x, y)] = DEAD  # DEAD를 추가한다.

while True:  # 프로그램의 메인 루프
    # 이 루프에서의 반복은 시뮬레이션의 단계다.

    print('\n' * 50)  # 각 단계를 개행 문자로 구분한다.
    cells = copy.deepcopy(nextCells)

    # 모든 셀을 화면에 출력한다:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # 문자 또는 공백을 출력한다.
        print()  # 한 행의 모든 열을 출력했다면 개행한다.
    print('Press Ctrl-C to quit.')

    # 현재 단계의 셀을 바탕으로 다음 단계의 셀을 계산한다:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # (x, y)의 주변 좌표를 가져온다.
            # 가장자리는 서로 연결되어 있다.
            left  = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # 주변에 살아 있는 셀을 센다:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # 왼쪽-상단 셀은 살아 있다.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # 상단 셀은 살아 있다.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # 오른쪽-상단 셀은 살아 있다.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # 왼쪽 셀은 살아 있다.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # 오른쪽 셀은 살아 있다.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # 왼쪽-하단 셀은 살아 있다.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # 하단 셀은 살아 있다.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # 오른쪽-하단 셀은 살아 있다.

            # 콘웨이의 라이프 게임 규칙을 기반으로 셀을 설정한다:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3):
                    # 현재 셀이 살아 있으면서 주변에 살아 있는 셀이 2 또는 3이면, 다음 단계에서도 살아 있는 셀이 된다:
                    nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # 현재 셀이 죽어 있으면서 주변에 살아 있는 셀이 3이면, 다음 단계에서 살아 있는 셀이 된다:
                nextCells[(x, y)] = ALIVE
            else:
                # 그 외의 모든 셀은 죽은 상태가 된다:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # 1초 동안 일시 중지하여 출력된 것을 확인할 수 있게 한다.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()  # Ctrl-C가 눌리면 프로그램을 종료한다.
