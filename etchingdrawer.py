"""Etching Drawer, by Al Sweigart al@inventwithpython.com
An art program that draws a continuous line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Or an even larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic"""

import shutil, sys

# 선 문자에 대한 상수 설정하기:
UP_DOWN_CHAR         = chr(9474)  # 캐릭터 9474는 '│'
LEFT_RIGHT_CHAR      = chr(9472)  # 캐릭터 9472는 '─'
DOWN_RIGHT_CHAR      = chr(9484)  # 캐릭터 9484는 '┌'
DOWN_LEFT_CHAR       = chr(9488)  # 캐릭터 9488은 '┐'
UP_RIGHT_CHAR        = chr(9492)  # 캐릭터 9492는 '└'
UP_LEFT_CHAR         = chr(9496)  # 캐릭터 9496은 '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # 캐릭터 9500은 '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # 캐릭터 9508은 '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # 캐릭터 9516은 '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # 캐릭터 9524는 '┴'
CROSS_CHAR           = chr(9532)  # 캐릭터 9532는 '┼'
# chr() 코드들에 대한 목록은 https://inventwithpython.com/chr를 참고하자.

# 터미널 창의 크기 얻기:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# 자동으로 줄바꿈을 추가하지 않으면 윈도우즈에서 마지막 열을 출력할 수 없으므로,
# 폭을 하나 줄인다.
CANVAS_WIDTH -= 1
# 명령어에 대한 정보를 표시하기 위해 하단 몇 줄을 띄어 놓는다.
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """Returns a multiline string of the line drawn in canvasData."""
    canvasStr = ''

    """canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            # 이 위치에 대한 선(라인) 문자를 canvasStr에 추가한다.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n'  # 각 행의 끝에 줄바꿈을 추가한다.
    return canvasStr


moves = []
while True:  # 메인 프로그램 루프
    # canvas에 있는 데이터를 바탕으로 선 그리기:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD keys to move, H for help, C to clear, '
        + 'F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()  # 프로그램 종료하기
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}  # 캔버스 데이터 지우기
        moves.append('C')  # 이에 대해 저장한다.
    elif response == 'F':
        # canvas 문자열을 텍스트 파일에 저장하기:
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            # 파일명 뒤에 .txt가 붙어 있는지 확인한다:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # 이외의 문자는 무시하고 다음 명령을 기다린다.
        moves.append(command)  # 이에 대해 저장한다.

        # 첫 번째로 추가되는 선은 전체 값의 형태로 저장되어야 한다:
        if canvas == {}:
            if command in ('W', 'S'):
                # 첫 번째로 추가되는 선을 가로 줄로 만든다:
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # 첫 번째로 추가되는 선을 세로 줄로 만든다:
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        # x와 y를 갱신한다:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # 커서가 캔버스 범위 밖으로 움직이려고 하므로,
            # 커서를 움직이지 않고
            # canvas[(cursorX, cursorY)]의 값을 바꾸지 않는다.
            continue

        # 만약에 (cursorX, cursorY)에 대한 set이 없다면, 빈 set를 추가한다:
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # 방향에 대한 문자열을 xy 위치 set에 추가한다:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
