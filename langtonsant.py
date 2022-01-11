"""Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, bext, simulation"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
WIDTH, HEIGHT = bext.size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다.
WIDTH -= 1
HEIGHT -= 1  # 하단의 종료 메시지를 위한 조정.

NUMBER_OF_ANTS = 10  # (!) 이 값을 1 또는 50으로 바꿔 보자.
PAUSE_AMOUNT = 0.1  # (!) 이 값을 1.0 또는 0.0으로 바꿔 보자.

# (!) 각 방향마다 다른 모양이 되도록 변경해 보자:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) 이 색상들을 'black', 'red', 'green', 'yellow',
# 'blue', 'purple', 'cyan', 'white' 중 하나로 바꿔 보자.
# (이 색상들은 bext 모듈이 지원하는 유일한 색상이다.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)  # 개미의 색상은 포그라운드 색상이다.
    bext.bg(WHITE_TILE)  # 백그라운드를 흰색으로 설정한다.
    bext.clear()

    # 새로운 보드 데이터 구조를 생성한다:
    board = {'width': WIDTH, 'height': HEIGHT}

    # 개미 데이터 구조를 생성한다:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # 어떤 타일이 변경되었는지 추적하고
    # 화면에 다시 그려야 한다:
    changedTiles = []

    while True:  # 메인 프로그램 루프
        displayBoard(board, ants, changedTiles)
        changedTiles = []

        # nextBoard는 시뮬레이션에서의 다음 단계 보드 모양이다.
        # 현재 단계의 보드를 복사하여 시작한다:
        nextBoard = copy.copy(board)

        # 각 개미에 대해 한 단계씩 시뮬레이션을 실행한다:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # 시계 방향으로 회전하기:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                # 반시계 방향으로 회전하기:
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changedTiles.append((ant['x'], ant['y']))

            # 개미가 향하는 방향과 상관없이 앞으로 이동한다:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1

            # 개미가 화면 가장자리를 지나게 된다면,
            # 반대쪽으로 나오도록 한다.
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], ant['y']))

        board = nextBoard


def displayBoard(board, ants, changedTiles):
    """화면에 보드와 개미를 표시한다. 
    changedTiles 인수는 변경되어 다시 그려야 하는 화면상의 타일에 대한
    (x, y) 튜플 리스트다."""

    # 보드 데이터 구조 그리기:
    for x, y in changedTiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        antIsHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antIsHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not antIsHere:
            print(' ', end='')

    # 화면 하단에 종료 메시지 표시하기:
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()  # (bext를 사용하는 프로그램에 필요하다.)
    time.sleep(PAUSE_AMOUNT)


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Langton's Ant, by Al Sweigart al@inventwithpython.com")
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
