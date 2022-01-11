"""Maze 3D, by Al Sweigart al@inventwithpython.com
Move around a maze and try to escape... in 3D!
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: extra-large, artistic, maze, game"""

import copy, sys, os

# 상수 설정하기:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Character 9617은 '░'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wallStrToWallDict(wallStr):
    """벽 그림을 나타내는 문자열(ALL_OPEN 또는 CLOSED 등)을 받아서
    (x, y) 튜플을 키로 사용하고,
    해당 위치에 그릴 아스키 아트에 대한 단일 문자열을 사용하는
    딕셔너리를 반환한다."""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# 표시할 문자열을 생성하는 방법은 wallStrToWallDict()를 이용하여
# 여러 줄의 문자열로 된 그림을 딕셔너리로 변환하는 것이다.
# 그런 다음 ALL_OPEN의 벽 딕셔너리 위에
# CLOSED의 벽 딕셔너리를 '붙여 넣어'
# 플레이어의 위치와 방향에 대한 벽을 구성한다.

ALL_OPEN = wallStrToWallDict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# strip() 호출은 여러 줄의 문자열의 시작 부분에서
# 줄바꿈을 제거하는 데 사용된다.

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
_____
.....
.....
.....
_____'''.strip()) # 좌표 6, 4에 붙인다.

CLOSED['B'] = wallStrToWallDict(r'''
.\.
..\
...
...
...
../
./.'''.strip()) # 좌표 4, 3에 붙인다.

CLOSED['C'] = wallStrToWallDict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip()) # 좌표 3, 1에 붙인다.

CLOSED['D'] = wallStrToWallDict(r'''
./.
/..
...
...
...
\..
.\.'''.strip()) # 좌표 10, 3에 붙인다.

CLOSED['E'] = wallStrToWallDict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip()) # 좌표 0, 0에 붙인다.

CLOSED['F'] = wallStrToWallDict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip()) # 좌표 12, 0에 붙인다.

def displayWallDict(wallDict):
    """wallStrToWallDict()에 의해 반환된 벽 딕셔너리를
    화면에 표시한다."""
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            wall = wallDict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)  # 블록을 인쇄한다.
    print(BLOCK * (wallDict['width'] + 2))


def pasteWallDict(srcWallDict, dstWallDict, left, top):
    """벽을 나타내는 딕셔너리 srcWallDict에 left와 top에 지정된 위치만큼
    오프셋을 적용한 dstWallDict를 만든다."""
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict


def makeWallDict(maze, playerx, playery, playerDirection, exitx, exity):
    """미로에서 플레이어의 위치와 방향
    (exitx, exity에 출구가 있음)을 가지고,
    벽을 나타내는 딕셔너리를 생성하여 반환한다."""

    # A-F '섹션'(플레이어의 방향에 대한)은
    # 우리가 만들고 있는 벽을 표현하는 딕셔너리 위에 붙여넣어야 하는지 확인하기 위해
    # 확인할 미로의 벽을 결정한다.

    if playerDirection == NORTH:
        # 플레이어 @을 기준으로 한   A
        # 섹션 지도:             BCD (플레이어가 북쪽을 향하고 있다)
        #                      E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        # 플레이어 @을 기준으로 한  F@E
        # 섹션 지도:             DCB (플레이어가 남쪽을 향하고 있다)
        #                       A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        # 플레이어 @을 기준으로 한   EB
        # 섹션 지도:              @CA (플레이어가 동쪽을 향하고 있다)
        #                       FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        # 플레이어 @을 기준으로 한   DF
        # 섹션 지도:              AC@ (플레이어가 서쪽을 향하고 있다)
        #                       BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff, playery + yOff), WALL)
        if (playerx + xOff, playery + yOff) == (exitx, exity):
            section[sec] = EXIT

    wallDict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wallDict = pasteWallDict(CLOSED[sec], wallDict,
                PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # 필요하다면 EXIT 표시를 그린다:
    if section['C'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 7, 9)
    if section['E'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 0, 11)
    if section['F'] == EXIT:
        wallDict = pasteWallDict(EXIT_DICT, wallDict, 13, 11)

    return wallDict


print('Maze Runner 3D, by Al Sweigart al@inventwithpython.com')
print('(Maze files are generated by mazemakerrec.py)')

# 사용자로부터 미로 파일의 파일명을 받는다:
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    # 현재 폴더에 있는 모든 미로 파일들을 나열한다:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze')
            and fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# 파일로부터 미로를 로드한다:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
px = None
py = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            px, py = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert px != None and py != None, 'No start point in file.'
assert exitx != None and exity != None, 'No exit point in file.'
pDir = NORTH


while True:  # 메인 게임 루프
    displayWallDict(makeWallDict(maze, px, py, pDir, exitx, exity))

    while True: # 사용자의 이동을 받는다.
        print('Location ({}, {})  Direction: {}'.format(px, py, pDir))
        print('                   (W)')
        print('Enter direction: (A) (D)  or QUIT.')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Please enter one of F, L, or R (or W, A, D).')
            continue

        # 플레이어를 의도한 방향으로 이동시킨다:
        if move == 'F' or move == 'W':
            if pDir == NORTH and maze[(px, py - 1)] == EMPTY:
                py -= 1
                break
            if pDir == SOUTH and maze[(px, py + 1)] == EMPTY:
                py += 1
                break
            if pDir == EAST and maze[(px + 1, py)] == EMPTY:
                px += 1
                break
            if pDir == WEST and maze[(px - 1, py)] == EMPTY:
                px -= 1
                break
        elif move == 'L' or move == 'A':
            pDir = {NORTH: WEST, WEST: SOUTH,
                    SOUTH: EAST, EAST: NORTH}[pDir]
            break
        elif move == 'R' or move == 'D':
            pDir = {NORTH: EAST, EAST: SOUTH,
                    SOUTH: WEST, WEST: NORTH}[pDir]
            break
        elif move.startswith('T'):  # 치트 코드: 'T x,y'
            px, py = move.split()[1].split(',')
            px = int(px)
            py = int(py)
            break
        else:
            print('You cannot move in that direction.')

    if (px, py) == (exitx, exity):
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
