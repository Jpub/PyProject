"""Hourglass, by Al Sweigart al@inventwithpython.com
An animation of an hourglass with falling sand. Press Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
PAUSE_LENGTH = 0.2  # (!) 이 값은 0.0 또는 1.0으로 바꿔 보자.
# (!) 이 값을 0과 100 사이의 값으로 바꿔 보자.
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # (x, y) 튜플에서의 X 값의 인덱스는 0이다.
Y = 1  # (x, y) 튜플에서의 Y 값의 인덱스는 1이다.
SAND = chr(9617)
WALL = chr(9608)

# 모래시계의 벽을 설정한다:
HOURGLASS = set()  # 모래시계 벽이 있는 위치에 대한 (x, y) 튜플을 갖는다.
# (!) 벽을 없애기 위해 HOURGLASS.add() 코드를 주석 처리해 보자:
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # 모래시계의 상단에 벽을 추가한다.
    HOURGLASS.add((i, 23))  # 하단에 벽을 추가한다.
for i in range(1, 5):
    HOURGLASS.add((18, i))  # 왼쪽 상단에 직선 벽을 추가한다.
    HOURGLASS.add((36, i))  # 오른쪽 상단에 직선 벽을 추가한다.
    HOURGLASS.add((18, i + 19))  # 왼쪽 하단에 벽을 추가한다.
    HOURGLASS.add((36, i + 19))  # 오른쪽 하단에 벽을 추가한다.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # 왼쪽 상단에 대각선 벽을 추가한다.
    HOURGLASS.add((35 - i, 5 + i))  # 오른쪽 상단에 대각선 벽을 추가한다.
    HOURGLASS.add((25 - i, 13 + i))  # 왼쪽 하단에 대각선 벽을 추가한다.
    HOURGLASS.add((29 + i, 13 + i))  # 오른쪽 하단에 대각선 벽을 추가한다.

# 모래시계의 상단에 최초의 모래를 준비한다:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # 종료 메시지를 그린다:
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # 모래시계의 벽을 표시한다:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # 메인 프로그램 루프
        allSand = list(INITIAL_SAND)

        # 최초 모래 그리기:
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        runHourglassSimulation(allSand)


def runHourglassSimulation(allSand):
    """모래가 더 이상 움직이지 않을 때까지
    시뮬레이션을 계속 실행한다."""
    while True:  # 모래가 다 떨어질 때까지 계속 반복한다.
        random.shuffle(allSand)  # 무작위로 섞는다.

        sandMovedOnThisStep = False
        for i, sand in enumerate(allSand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # 모래가 맨 아래에 있으므로, 더 이상 움직이지 않는다:
                continue

            # 이 모래 밑에 아무것도 없다면 아래로 이동한다:
            noSandBelow = (sand[X], sand[Y] + 1) not in allSand
            noWallBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noWallBelow

            if canFallDown:
                # 한 칸 아래의 새 위치에 모래를 그린다:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # 이전 위치를 지운다.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # 한 칸 아래의 새 위치에 모래를 설정한다:
                allSand[i] = (sand[X], sand[Y] + 1)
                sandMovedOnThisStep = True
            else:
                # 모래가 왼쪽으로 떨어질 수 있는지 확인한다:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in allSand
                noWallBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noWallLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = (noSandBelowLeft and noWallBelowLeft
                    and noWallLeft and notOnLeftEdge)

                # 모래가 오른쪽으로 떨어질 수 있는지 확인한다:
                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in allSand
                noWallBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noWallRight = right not in HOURGLASS
                notOnRightEdge = sand[X] < SCREEN_WIDTH - 1
                canFallRight = (noSandBelowRight and noWallBelowRight
                    and noWallRight and notOnRightEdge)

                # 떨어지는 방향을 설정한다:
                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1  # 모래가 왼쪽으로 떨어지도록 설정한다.
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1  # 모래가 오른쪽으로 떨어지도록 설정한다.
                elif canFallLeft and canFallRight:
                    # 양쪽 모두 가능하다면 무작위로 선택하여 설정한다:
                    fallingDirection = random.choice((-1, 1))

                # 모래가 왼쪽이나 오른쪽으로 단 한 칸이 아니라,
                # 두 칸 떨어질 수 있는지 확인한다:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in allSand
                    noWallBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = (canFallLeft and noSandBelowTwoLeft
                        and noWallBelowTwoLeft and notOnSecondToLeftEdge)

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in allSand
                    noWallBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] < SCREEN_WIDTH - 2
                    canFallTwoRight = (canFallRight
                        and noSandBelowTwoRight and noWallBelowTwoRight
                        and notOnSecondToRightEdge)

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    # 이 모래는 떨어질 수 없으므로, 계속 진행한다.
                    continue

                # 새로운 위치에 모래를 그린다:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # 이전 모래를 지운다.
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')  # 새로운 모래를 그린다.

                # 모래 알갱이를 새로운 위치로 이동한다:
                allSand[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()  # (bext를 사용하는 프로그램에 필요하다.)
        time.sleep(PAUSE_LENGTH)  # 잠깐 멈춘다.

        # 이 단계에서 이동한 모래가 없다면, 모래시계를 다시 설정한다:
        if not sandMovedOnThisStep:
            time.sleep(2)
            # 모든 모래를 지운다:
            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break  # 메인 시뮬레이션 루프에서 빠져나온다.


# 이 프로그램이 다른 프로그램에 임포트(import)된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
