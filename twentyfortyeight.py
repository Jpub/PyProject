"""Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com
A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.
More info at https://en.wikipedia.org/wiki/2048_(video_game)
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, puzzle"""

import random, sys

# 상수 설정하기:
BLANK = ''  # 보드의 빈칸을 나타내는 값


def main():
    print('''Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com

Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up the tiles before then.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()

    while True:  # 메인 게임 루프
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def getNewBoard():
    """보드를 나타내는 새로운 데이터 구조를 반환한다.

    (x, y) 튜플의 키와 해당 공간의 타일 값이 있는 딕셔너리다.
    타일은 2의 제곱수 또는 공백이다.
    좌표는 다음과 같다:
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""

    newBoard = {}  # 반환할 보드 데이터 구조를 담는다.
    # 가능한 모든 공간에 대해 루프를 돌면서 모든 타일을 공백으로 설정한다:
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # 2개의 2로 시작하기 위해 2개의 임의 칸을 고른다:
    startingTwosPlaced = 0  # 선택된 시작 칸의 수
    while startingTwosPlaced < 2:  # 중복된 칸에 대해 다시 반복한다.
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # 임의로 선택한 칸이 이미 사용되고 있는 건 아닌지 확인한다:
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1

    return newBoard


def drawBoard(board):
    """보드 데이터 구조를 화면에 그린다."""

    # 왼쪽에서 오른쪽으로, 위에서 아래로 각 칸에 대해 살펴보고,
    # 각 칸의 레이블에 대한 리스트를 생성한다.
    labels = []  # 해당 타일에 대한 숫자/빈칸의 문자열 리스트
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]  # 이 칸의 타일을 가져온다.
            # 레이블이 5칸 길이인지 확인한다:
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # {}는 그 타일에 대한 레이블로 교체한다:
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def getScore(board):
    """보드 데이터 구조에 있는 모든 타일의 합계를 반환한다."""
    score = 0
    # 모든 공간에 대해 루프를 돌고 스코어에 타일을 더한다:
    for x in range(4):
        for y in range(4):
            # 스코어에 빈 타일이 아닌 것만 더한다:
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combineTilesInColumn(column):
    """열은 4개의 타일 리스트다.
    인덱스 0은 열의 '하단'이고 타일은 서로 동일한 경우에 합쳐진다.
    예를 들어 CombineTilesInColumn([2, BLANK, 2, 공백])의 경우,
    [4, 공백, 공백, 공백]을 반환한다."""

    # column의 값들 중에 공백이 아닌 숫자만 combinedTiles에 복사한다:
    combinedTiles = []  # column의 값들 중 공백이 아닌 타일들의 목록
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])

    # 4개의 타일이 될 때까지 공백을 계속 추가하기:
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    # 현재의 숫자와 다음의 숫자가 서로 같다면 서로 합하여 두 배가 되게 한다.
    for i in range(3):  # 인덱스 3은 최상단의 공간이기 때문에 건너뛴다.
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2  # 이 타일의 숫자를 두 배로 한다.
            # 위 타일을 한 칸 아래로 이동한다:
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK  # 최상위 공간은 항상 BLANK다.
    return combinedTiles


def makeMove(board, move):
    """보드에서 이동을 수행한다.

    이동 인수는 'W', 'A', 'S' 또는 'D'이고,
    이 함수는 최종 보드 데이터 구조를 반환한다."""

    # 게임 보드는 이동하는 방향에 따라
    # 4개의 열로 나뉜다:
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    # 이동한 후의 보드 데이터 구조:
    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:  # 4개의 모든 열에 대해 루프를 돈다.
        # 이 열의 타일들을 얻는다:
        # (첫 번째 타일은 그 열의 밑(bottom)이다)
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        # 열에 있는 타일들을 합친다:
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        # 조합된 타일들로 새로운 보드 데이터 구조를 만든다:
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def askForPlayerMove():
    """플레이어에게 다음 이동 방향(또는 종료)을 묻는다.

    유효한 동작인 'W', 'A', 'S' 또는 'D' 중 하나를 입력했는지 확인한다."""
    print('Enter move: (WASD or Q to quit)')
    while True:  # 유효한 움직임이 입력될 때까지 루프를 계속 돈다.
        move = input('> ').upper()
        if move == 'Q':
            # 프로그램 종료:
            print('Thanks for playing!')
            sys.exit()

        # 유효한 움직임을 반환하거나, 루프로 돌아가면서 사용자 입력을 다시 요청한다:
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')


def addTwoToBoard(board):
    """보드에 새로운 타일 2개를 무작위로 추가한다."""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return  # 비어 있지 않은 타일 하나를 찾은 후 반환한다.


def isFull(board):
    """보드 데이터 구조에 공백이 없으면 True를 반환한다."""
    # 보드의 모든 칸에 대해 루프를 돈다:
    for x in range(4):
        for y in range(4):
            # 빈칸이면 False를 반환한다:
            if board[(x, y)] == BLANK:
                return False
    return True  # 빈칸이 없으므로 True를 반환한다.


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
