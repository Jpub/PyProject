"""Mondrian Art Generator, by Al Sweigart al@inventwithpython.com
Randomly generates art in the style of Piet Mondrian.
More info at: https://en.wikipedia.org/wiki/Piet_Mondrian
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, bext"""

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# 화면 설정하기:
width, height = bext.size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다:
width -= 1

height -= 3

while True:  # 메인 애플리케이션 루프.
    # 캔버스를 빈 공간으로 미리 채운다:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    # 수직선 생성하기:
    numberOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        numberOfSegmentsToDelete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # 수평선 생성하기:
    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        numberOfSegmentsToDelete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numberOfRectanglesToPaint = numberOfSegmentsToDelete - 3
    numberOfSegmentsToDelete = int(numberOfSegmentsToDelete * 1.5)

    # 무작위로 점을 선택하고 제거한다.
    for i in range(numberOfSegmentsToDelete):
        while True:  # 삭제할 세그먼트를 계속 선택한다.
            # 기존의 세그먼트에서 임의의 시작점 가져오기:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            if canvas[(startx, starty)] == WHITE:
                continue

            # 수직 또는 수평 세그먼트에 있는지 확인하기:
            if (canvas[(startx - 1, starty)] == WHITE and
                canvas[(startx + 1, starty)] == WHITE):
                orientation = 'vertical'
            elif (canvas[(startx, starty - 1)] == WHITE and
                canvas[(startx, starty + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                # 시작점이 교차 지점에 있으므로,
                # 새로운 임의의 시작점을 구한다:
                continue

            pointsToDelete = [(startx, starty)]

            canDeleteSegment = True
            if orientation == 'vertical':
                # 시작점에서 한 경로 위로 이동하고,
                # 이 세그먼트를 제거할 수 있는지 확인한다:
                for changey in (-1, 1):
                    y = starty
                    while 0 < y < height - 1:
                        y += changey
                        if (canvas[(startx - 1, y)] == BLACK and
                            canvas[(startx + 1, y)] == BLACK):
                            # 우리는 네 방향 교차점을 찾았다.
                            break
                        elif ((canvas[(startx - 1, y)] == WHITE and
                               canvas[(startx + 1, y)] == BLACK) or
                              (canvas[(startx - 1, y)] == BLACK and
                               canvas[(startx + 1, y)] == WHITE)):
                            # 우리는 세 방향 교차점을 찾았다.
                            # 이 세그먼트는 삭제할 수 없다:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((startx, y))

            elif orientation == 'horizontal':
                # 시작점에서 한 경로 위로 이동하고,
                # 이 세그먼트를 제거할 수 있는지 확인한다:
                for changex in (-1, 1):
                    x = startx
                    while 0 < x < width - 1:
                        x += changex
                        if (canvas[(x, starty - 1)] == BLACK and
                            canvas[(x, starty + 1)] == BLACK):
                            # 우리는 네 방향 교차점을 찾았다.
                            break
                        elif ((canvas[(x, starty - 1)] == WHITE and
                               canvas[(x, starty + 1)] == BLACK) or
                              (canvas[(x, starty - 1)] == BLACK and
                               canvas[(x, starty + 1)] == WHITE)):
                            # 우리는 세 방향 교차점을 찾았다;
                            # 이 세그먼트는 삭제할 수 없다:
                            canDeleteSegment = False
                            break
                        else:
                            pointsToDelete.append((x, starty))
            if not canDeleteSegment:
                continue  # 새로운 임의의 시작점을 구한다:
            break  # 세그먼트를 삭제하기 위해 이동한다.

        # 이 세그먼트를 삭제할 수 있다면, 모든 점을 흰색으로 설정한다:
        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    # 테두리를 추가하기:
    for x in range(width):
        canvas[(x, 0)] = BLACK  # 상단 테두리
        canvas[(x, height - 1)] = BLACK  # 하단 테두리
    for y in range(height):
        canvas[(0, y)] = BLACK  # 좌측 테두리
        canvas[(width - 1, y)] = BLACK  # 우측 테두리

    # 직사각형 색칠하기:
    for i in range(numberOfRectanglesToPaint):
        while True:
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)

            if canvas[(startx, starty)] != WHITE:
                continue  # 새로운 임의의 시작점을 구한다:
            else:
                break

        # 플러드 필(Flood fill) 알고리즘:
        colorToPaint = random.choice([RED, YELLOW, BLUE, BLACK])
        pointsToPaint = set([(startx, starty)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            canvas[(x, y)] = colorToPaint
            if canvas[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    # 캔버스 데이터 구조 그리기:
    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(' ', end='')

        print()

    # 사용자에게 새로운 것을 생성하라는 메시지를 표시한다:
    try:
        input('Press Enter for another work of art, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()
