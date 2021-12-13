"""Sudoku Puzzle, by Al Sweigart al@inventwithpython.com
The classic 9x9 number placement puzzle.
More info at https://en.wikipedia.org/wiki/Sudoku
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, object-oriented, puzzle"""

import copy, random, sys

# 이 게임은 퍼즐이 포함된 sudokupuzzle.txt 파일이 필요하다.
# 이 파일은 https://inventwithpython.com/sudokupuzzles.txt 에서 다운로드받을 수 있다.
# 다음은 이 파일의 내용 중 일부다.
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# 2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3
# ......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34.59...5.7......
# .3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.

# 상수 설정하기:
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        # originalSetup은 숫자와 마침표(공백을 위함)가 포함된
        # 퍼즐 설정을 위한 81개의 문자열이다.
        # https://inventwithpython.com/sudokupuzzles.txt 참고
        self.originalSetup = originalSetup

        # 스도쿠 그리드의 상태는
        # (x, y) 키와 해당 칸에 대한 숫자 값(문자열)이 있는
        # 딕셔너리로 나타낸다.
        self.grid = {}
        self.resetGrid()  # 그리드 상태를 원래 설정으로 설정한다.
        self.moves = []  # 실행 취소 기능을 위해 이동에 대해 추적한다.

    def resetGrid(self):
        """Reset the state of the grid, tracked by self.grid, to the
        state in self.originalSetup."""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0  # i는 0에서 80까지 간다.
        y = 0  # y 0에서 8까지 간다.
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1

    def makeMove(self, column, row, number):
        """Place the number at the column (a letter from A to I) and row
        (an integer from 1 to 9) on the grid."""
        x = 'ABCDEFGHI'.find(column)  # 이것을 정수로 변환한다.
        y = int(row) - 1

        # 숫자가 채워진 곳인지 확인한다:
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number  # 이 숫자를 그리드에 배치한다.

        # 딕셔너리 객체의 별도 복사본을 저장해야 한다:
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """Set the current grid state to the previous state in the
        self.moves list."""
        if self.moves == []:
            return  # self.moves에 상태가 없으므로 아무것도 하지 않는다.

        self.moves.pop()  # 현재 상태를 제거한다.

        if self.moves == []:
            self.resetGrid()
        else:
            # 그리드를 마지막 이동으로 설정한다.
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """Display the current state of the grid on the screen."""
        print('   A B C   D E F   G H I')  # 열에 대한 레이블을 표시한다.
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # 행에 대한 레이블을 표시한다:
                    print(str(y + 1) + '  ', end='')

                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    # 수직선 표시한다:
                    print('| ', end='')
            print()  # 줄바꿈을 출력한다.

            if y == 2 or y == 5:
                # 수평선을 표시한다:
                print('   ------+-------+------')

    def _isCompleteSetOfNumbers(self, numbers):
        """Return True if numbers contains the digits 1 through 9."""
        return sorted(numbers) == list('123456789')

    def isSolved(self):
        """Returns True if the current grid is in a solved state."""
        # 각 행을 확인한다:
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        # 각 열을 확인한다:
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        # 각 하위 그리드를 확인한다:
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False

        return True


print('''Sudoku Puzzle, by Al Sweigart al@inventwithpython.com

Sudoku is a number placement logic puzzle game. A Sudoku grid is a 9x9
grid of numbers. Try to place numbers in the grid such that every row,
column, and 3x3 box has the numbers 1 through 9 once and only once.

For example, here is a starting Sudoku grid and its solved form:

    5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
    6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
    . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
    ------+-------+------     ------+-------+------
    8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
    4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
    7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
    ------+-------+------     ------+-------+------
    . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
    . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
    . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')
input('Press Enter to begin...')


# sudokupuzzles.txt 파일을 로드한다:
with open('sudokupuzzles.txt') as puzzleFile:
    puzzles = puzzleFile.readlines()

# 각 퍼즐의 끝에 줄바꿈을 제거한다:
for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True:  # 메인 게임 루프
    grid.display()

    # 퍼즐을 다 풀었는지 확인한다.
    if grid.isSolved():
        print('Congratulations! You solved the puzzle!')
        print('Thanks for playing!')
        sys.exit()

    # 플레이어의 동작을 얻는다:
    while True:  # 플레이어가 유효한 동작을 입력할 때까지 계속 요구한다.
        print()  # 줄바꿈을 출력한다.
        print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
        print('(For example, a move looks like "B4 9".)')

        action = input('> ').upper().strip()

        if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
            # 플레이어가 유효한 동작을 입력했다.
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                continue

            column, row = space
            if column not in list('ABCDEFGHI'):
                print('There is no column', column)
                continue
            if not row.isdecimal() or not (1 <= int(row) <= 9):
                print('There is no row', row)
                continue
            if not (1 <= int(number) <= 9):
                print('Select a number from 1 to 9, not ', number)
                continue
            break  # 플레이어가 유효한 동작을 입력했다.

    print()  # 줄바꿈을 출력한다.

    if action.startswith('R'):
        # 그리드를 리셋한다:
        grid.resetGrid()
        continue

    if action.startswith('N'):
        # 새로운 퍼즐을 가져온다:
        grid = SudokuGrid(random.choice(puzzles))
        continue

    if action.startswith('U'):
        # 마지막 동작을 취소한다:
        grid.undo()
        continue

    if action.startswith('O'):
        # 원래 숫자를 본다:
        originalGrid = SudokuGrid(grid.originalSetup)
        print('The original grid looked like this:')
        originalGrid.display()
        input('Press Enter to continue...')

    if action.startswith('Q'):
        # 게임을 종료한다.
        print('Thanks for playing!')
        sys.exit()

    # 플레이어가 선택한 동작을 처리한다.
    if grid.makeMove(column, row, number) == False:
        print('You cannot overwrite the original grid\'s numbers.')
        print('Enter ORIGINAL to view the original grid.')
        input('Press Enter to continue...')
