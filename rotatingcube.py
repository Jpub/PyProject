"""Rotating Cube, by Al Sweigart al@inventwithpython.com
A rotating cube animation. Press Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, math"""

# 이번 프로그램은 반드시 터미널 또는 명령 프롬프트 창에서 실행되어야 한다.

import math, time, sys, os

# 상수 설정하기:
PAUSE_AMOUNT = 0.1  # 일시 중지 시간은 10분의 1초다.
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
# 텍스트 셀의 길이는 폭의 두 배이므로, scaley를 설정한다:
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

# (!) 이 값을 '#'이나 '*' 또는 다른 문자로 바꿔 보자:
LINE_CHAR = chr(9608)  # Character 9608은 꽉 찬 블록이다.

# (!) 단일 축에 따라 큐브를 회전하려면,
# 다음의 값들 중 2개를 0으로 설정하자:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# 이번 프로그램은 리스트에 XYZ 좌표를 저장한다.
# 인덱스 0에 X 좌표, 1에 Y 좌표, 2에 Z 좌표
# 이들 상수는 리스트의 좌표에 접근할 때 코드를 읽기 쉽게 해준다.
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []  # 라인의 위치를 담는다.
    # "Steep"은 라인이 45도보다 크거나
    # -45도보다 작다는 의미다:

    # 이 함수가 올바르게 처리하지 않는
    # 시작점과 끝점이 인접해 있는 특별한 경우에 대해 확인하여
    # 하드 코딩된 리스트를 반환한다:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        # 이 알고리즘은 가파르지 않은 라인만 처리하므로,
        # 기울기를 비경사(non-steep)로 변경하고 나중에 다시 돌려놓는다.
        x1, y1 = y1, x1  # x1과 y1을 바꾼다.
        x2, y2 = y2, x2  # x2와 y2를 바꾼다.
    isReversed = x1 > x2  # 라인이 오른쪽에서 왼쪽으로 가능 경우 True

    if isReversed:  # 오른쪽에서 왼쪽으로 가는 라인의 점을 가져온다.
        x1, x2 = x2, x1  # x1과 x2를 바꾼다.
        y1, y2 = y2, y1  # y1과 y2를 바꾼다.

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y2
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # 이 라인의 모든 x에 대한 y를 계산한다:
        for currentx in range(x2, x1 - 1, -1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray <= 0:  # extray <= 0인 경우에는 y만 변경한다.
                currenty -= ydirection
                extray += deltax
    else:  # 왼쪽에서 오른쪽으로 가는 라인의 점을 가져온다.
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        extray = int(deltax / 2)
        currenty = y1
        if y1 < y2:
            ydirection = 1
        else:
            ydirection = -1
        # 이 라인의 모든 x에 대한 y를 계산한다:
        for currentx in range(x1, x2 + 1):
            if isSteep:
                points.append((currenty, currentx))
            else:
                points.append((currentx, currenty))
            extray -= deltay
            if extray < 0:  # extray < 0인 경우에는 y만 변경한다.
                currenty += ydirection
                extray += deltax
    return points


def rotatePoint(x, y, z, ax, ay, az):
    """Returns an (x, y, z) tuple of the x, y, z arguments rotated.

    The rotation happens around the 0, 0, 0 origin by angles
    ax, ay, az (in radians).
        Directions of each axis:
         -y
          |
          +-- +x
         /
        +z
    """

    # x 축을 중심으로 회전한다:
    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # y 축을 중심으로 회전한다:
    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    # z 축을 중심으로 회전한다:
    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def adjustPoint(point):
    """Adjusts the 3D XYZ point to a 2D XY point fit for displaying on
    the screen. This resizes this 2D point by a scale of SCALEX and
    SCALEY, then moves the point by TRANSLATEX and TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX),
            int(point[Y] * SCALEY + TRANSLATEY))


"""CUBE_CORNERS stores the XYZ coordinates of the corners of a cube.
The indexes for each corner in CUBE_CORNERS are marked in this diagram:
      0---1
     /|  /|
    2---3 |
    | 4-|-5
    |/  |/
    6---7"""
CUBE_CORNERS = [[-1, -1, -1], # 포인트 0
                [ 1, -1, -1], # 포인트 1
                [-1, -1,  1], # 포인트 2
                [ 1, -1,  1], # 포인트 3
                [-1,  1, -1], # 포인트 4
                [ 1,  1, -1], # 포인트 5
                [-1,  1,  1], # 포인트 6
                [ 1,  1,  1]] # 포인트 7
# rx, ry, rz만큼 회전한 다음,
# CUBE_CORNERS의 XYZ 좌표를 rotatedCorners에 저장한다:
rotatedCorners = [None, None, None, None, None, None, None, None]
# 각 축의 회전량:
xRotation = 0.0
yRotation = 0.0
zRotation = 0.0

try:
    while True:  # 메인 프로그램 루프
        # 각 양만큼 각 축에 따라 회전한다:
        xRotation += X_ROTATE_SPEED
        yRotation += Y_ROTATE_SPEED
        zRotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotatedCorners[i] = rotatePoint(x, y, z, xRotation,
                yRotation, zRotation)

        # 큐브 라인의 점들을 얻는다:
        cubePoints = []
        for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
            fromX, fromY = adjustPoint(rotatedCorners[fromCornerIndex])
            toX, toY = adjustPoint(rotatedCorners[toCornerIndex])
            pointsOnLine = line(fromX, fromY, toX, toY)
            cubePoints.extend(pointsOnLine)

        # 중복된 점 제거하기:
        cubePoints = tuple(frozenset(cubePoints))

        # 화면에 큐브 표시하기:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cubePoints:
                    # 전체 블록 표시하기:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # 빈 공간 표시하기:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # 잠깐 멈춤

        # 화면 정리하기:
        if sys.platform == 'win32':
            os.system('cls')  # 윈도우즈는 cls 명령어를 사용한다.
        else:
            os.system('clear')  # macOS와 리눅스는 clear 명령어를 사용한다.

except KeyboardInterrupt:
    print('Rotating Cube, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
