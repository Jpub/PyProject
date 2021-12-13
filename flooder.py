"""Flooder, by Al Sweigart al@inventwithpython.com
A colorful game where you try to fill the board with a single color. Has
a mode for colorblind players.
Inspired by the "Flood It!" game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, bext, game"""

import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
BOARD_WIDTH = 16  # (!) 이 값을 4 또는 40으로 바꿔 보자.
BOARD_HEIGHT = 14  # (!) 이 값을 4 또는 20으로 바꿔 보자.
MOVES_PER_GAME = 20  # (!) 이 값을 3 또는 300으로 바꿔 보자.

# 색맹 모드(colorblind mode)에서 사용될 다양한 모양에 대한 상수:
HEART     = chr(9829)  # 문자 9829는 '♥'.
DIAMOND   = chr(9830)  # 문자 9830은 '♦'.
SPADE     = chr(9824)  # 문자 9824는 '♠'.
CLUB      = chr(9827)  # 문자 9827은 '♣'.
BALL      = chr(9679)  # 문자 9679는 '●'.
TRIANGLE  = chr(9650)  # 문자 9650은 '▲'.

BLOCK     = chr(9608)  # 문자 9608은 '█'
LEFTRIGHT = chr(9472)  # 문자 9472는 '─'
UPDOWN    = chr(9474)  # 문자 9474는 '│'
DOWNRIGHT = chr(9484)  # 문자 9484는 '┌'
DOWNLEFT  = chr(9488)  # 문자 9488은 '┐'
UPRIGHT   = chr(9492)  # 문자 9492는 '└'
UPLEFT    = chr(9496)  # 문자 9496은 '┘'
# chr() 코드의 전체 목록은 https://inventwithpython.com/chr를 참고하자.

# 게임에 사용되는 모든 색상/모양 타일:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Al Sweigart al@inventwithpython.com

Set the upper left color/shape, which fills in all the
adjacent squares of that color/shape. Try to make the
entire board the same color/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:  # 메인 게임 루프
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def getNewBoard():
    """Return a dictionary of a new Flood It board."""

    # 키는 (x, y) 튜플이고, 값은 그 위치의 타일이다.
    board = {}

    # 랜덤하게 색상을 생성한다.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # 몇 개의 타일은 주변과 같도록 한다.
    # 이것은 동일한 색상/모양의 타일 그룹을 만든다.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board, displayMode):
    """Display the board on the screen."""
    bext.fg('white')
    # 게임의 상단 면을 표시한다:
    print(DOWNRIGHT + (LEFTRIGHT * BOARD_WIDTH) + DOWNLEFT)

    # 각 열을 표시한다:
    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0:  # 첫 번째 열은 '>'로 시작한다.
            print('>', end='')
        else:  # 이후의 열들은 흰색 수직선으로 시작한다.
            print(UPDOWN, end='')

        # 이 열의 각 타일을 표시한다:
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if displayMode == COLOR_MODE:
                print(BLOCK, end='')
            elif displayMode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN)  # 각 열은 흰색 수직선으로 끝난다.
    # 게임의 하단 면을 표시한다:
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


def askForPlayerMove(displayMode):
    """Let the player select a color to paint the upper left tile."""
    while True:
        bext.fg('white')
        print('Choose one of ', end='')

        if displayMode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif displayMode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart, ', end='')
            bext.fg('green')
            print('(T)riangle, ', end='')
            bext.fg('blue')
            print('(D)iamond, ', end='')
            bext.fg('yellow')
            print('(B)all, ', end='')
            bext.fg('cyan')
            print('(C)lub, ', end='')
            bext.fg('purple')
            print('(S)pade, ', end='')
        bext.fg('white')
        print('or QUIT:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if displayMode == COLOR_MODE and response in tuple('RGBYCP'):
            # 사용자의 입력에 따라 타일 타입 번호를 반환한다:
            return {'R': 0, 'G': 1, 'B': 2,
                'Y': 3, 'C': 4, 'P': 5}[response]
        if displayMode == SHAPE_MODE and response in tuple('HTDBCS'):
            # 사용자의 입력에 따라 타일 타입 번호를 반환한다:
            return {'H': 0, 'T': 1, 'D':2,
                'B': 3, 'C': 4, 'S': 5}[response]


def changeTile(tileType, board, x, y, charToChange=None):
    """Change the color/shape of a tile using the recursive flood fill
    algorithm."""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return  # 기본 조건: 이미 동일한 타일이다.

    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        # 재귀 조건: 왼쪽 타일을 변경한다:
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        # 재귀 조건: 윗쪽 타일을 변경한다:
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        # 재귀 조건: 오른쪽 타일을 변경한다:
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        # 재귀 조건: 아래쪽 타일을 변경한다:
        changeTile(tileType, board, x, y + 1, charToChange)


def hasWon(board):
    """Return True if the entire board is one color/shape."""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
