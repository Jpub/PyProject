"""Maze Runner 2D, by Al Sweigart al@inventwithpython.com
Move around a maze and try to escape. Maze files are generated by
mazemakerrec.py.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, maze"""

import sys, os

# 미로 파일 상수:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'  # (!) 이 값을 '+' 또는 'o'로 바꿔 보자.
BLOCK = chr(9617)  # Character 9617은 '░'


def displayMaze(maze):
    # 미로 표시하기:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()  # 행을 출력한 후, 개행을 인쇄한다.


print('''Maze Runner 2D, by Al Sweigart al@inventwithpython.com

(Maze files are generated by mazemakerrec.py)''')

# 미로 파일의 파일명을 사용자로부터 받는다:
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    # 현재 폴더에 있는 모든 미로 파일을 나열한다:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and
            fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# 파일에서 미로 로드하기:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
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
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'No start in maze file.'
assert exitx != None and exity != None, 'No exit in maze file.'

while True:  # 메인 게임 루프
    displayMaze(maze)

    while True:  # 사용자의 움직임을 받는다.
        print('                           W')
        print('Enter direction, or QUIT: ASD')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print('Invalid direction. Enter one of W, A, S, or D.')
            continue

        # 플레이어가 그 방향으로 이동할 수 있는지 확인한다:
        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print('You cannot move in that direction.')

    # 분기점을 만날 때까지 그 방향으로 계속 이동한다.
    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break  # 벽에 부딪히면 빠져나온다.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # 분기점에 다다르면 빠져나온다.
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break  # 벽에 부딪히면 빠져나온다.
            if (maze[(playerx - 1, playery)] == EMPTY
                or maze[(playerx + 1, playery)] == EMPTY):
                break  # 분기점에 다다르면 빠져나온다.
    elif move == 'A':
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                break  # 벽에 부딪히면 빠져나온다.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # 분기점에 다다르면 빠져나온다.
    elif move == 'D':
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                break  # 벽에 부딪히면 빠져나온다.
            if (maze[(playerx, playery - 1)] == EMPTY
                or maze[(playerx, playery + 1)] == EMPTY):
                break  # 분기점에 다다르면 빠져나온다.

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
