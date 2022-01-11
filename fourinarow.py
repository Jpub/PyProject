"""Four in a Row, by Al Sweigart al@inventwithpython.com
A tile-dropping game to get four in a row, similar to Connect Four.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, board game, two-player"""

import sys

# 보드를 표시하기 위해 사용되는 상수들:
EMPTY_SPACE = '.'  # 공백보다 점(period)이 카운팅에 용이하다.
PLAYER_X = 'X'
PLAYER_O = 'O'

# 참고: 만약에 BOARD_WIDTH를 바꾼다면 displayBoard()와 COLUMN_LABELS를 업데이트하자.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print("""Four in a Row, by Al Sweigart al@inventwithpython.com

Two players take turns dropping tiles into one of seven columns, trying
to make four in a row horizontally, vertically, or diagonally.
""")

    # 새로운 게임 설정:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:  # 플레이어의 차례를 실행한다.
        # 보드를 표시하고 플레이어의 움직임을 얻는다:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # 이겼는지 비겼는지 확인:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # 마지막으로 보드를 표시한다.
            print('Player ' + playerTurn + ' has won!')
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)  # 마지막으로 보드를 표시한다.
            print('There is a tie!')
            sys.exit()

        # 다른 플레이어에게 차례를 넘김:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """Four in a Row 보드를 나타내는 딕셔너리를 반환한다.

    키는 두 개의 정수인 (columnIndex, rowIndex) 튜플이며,
    값은 'X', 'O' 또는 '.'(빈 공간) 문자열 중 하나다."""
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """보드와 타일을 화면에 표시한다."""

    '''보드 템플릿의 format() 문자열 메서드에 전달할 리스트를 준비한다.
    리스트에는 왼쪽에서 오른쪽으로, 그리고
    위에서 아래로 이동하는 보드의 모든 타일(및 빈 공간)이 있다.'''
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # 보드 표시하기:
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars))


def askForPlayerMove(playerTile, board):
    """플레이어가 타일을 놓을 보드의 열을 선택하게 한다.

    타일이 놓이는 (열, 행) 튜플을 반환한다."""
    while True:  # 유효한 입력을 할 때까지 계속 물어 본다.
        print('Player {}, enter a column or QUIT:'.format(playerTile))
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue  # 플레이어에게 다시 물어 본다.

        columnIndex = int(response) - 1  # 0 기반의 인덱스를 위해 -1한다.

        # 모든 열이 가득 차면 다시 물어 본다:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue  # 플레이어에게 다시 물어 봄.

        # 바닥부터 시작하여 첫 번째 빈 공간을 찾는다.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    """보드에 빈 공간이 없다면 True를 반환하고,
    그렇지 않으면 False를 반환한다."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # 빈 공간을 찾았으므로 False를 반환한다.
    return True  # 모든 공간이 찼다.


def isWinner(playerTile, board):
    """playerTile'이 'board'에 연속으로 4개의 타일을 가지고 있으면 True를 반환하고,
     그렇지 않으면 False를 반환한다."""

    # 전체 보드에 대해 four-in-a-row을 검사한다:
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # 수평으로 four-in-a-row인지 확인한다:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 수직으로 four-in-a-row인지 확인한다:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 오른쪽 아래 대각선으로 four-in-a-row인지 확인한다:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # 왼쪽 아래 대각선으로 four-in-a-row인지 확인한다:
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
