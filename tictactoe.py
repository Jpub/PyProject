"""Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
The classic board game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, board game, game, two-player"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # 문자열 값에 대한 상수


def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()  # 틱-택-토 보드 딕셔너리를 생성한다.
    currentPlayer, nextPlayer = X, O  # X가 먼저 나오고, 그 다음에 O가 나온다.

    while True:  # 메인 게임 루프
        # 화면에 보드 표시하기:
        print(getBoardStr(gameBoard))

        # 사용자가 1-9 숫자를 입력할 때까지 계속 요청한다:
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)  # 턴을 진행한다.

        # 게임이 끝났는지 확인한다:
        if isWinner(gameBoard, currentPlayer):  # 승자를 확인한다.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):  # 무승부인지 확인한다.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        # 다음 플레이어 턴으로 바꾼다:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    """Create a new, blank tic-tac-toe board."""
    # 빈칸에 대한 번호: 1|2|3
    #                -+-+-
    #                4|5|6
    #                -+-+-
    #                7|8|9
    # 키는 1부터 9이고, 값은 X, O, 또는 BLANK:
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # 모든 칸을 빈칸으로 시작한다.
    return board


def getBoardStr(board):
    """Return a text-representation of the board."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
    and the space is blank."""
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    """Return True if player is a winner on this TTTBoard."""
    # 가독성을 위해 여기에 사용된 짧은 변수 이름:
    b, p = board, player
    # 행 3개, 열 3개, 대각선 2개에 걸쳐 표시가 있는지 확인한다.
    return ((b['1'] == b['2'] == b['3'] == p) or  # 상단 행
            (b['4'] == b['5'] == b['6'] == p) or  # 중단 행
            (b['7'] == b['8'] == b['9'] == p) or  # 하단 행
            (b['1'] == b['4'] == b['7'] == p) or  # 왼쪽 열
            (b['2'] == b['5'] == b['8'] == p) or  # 중앙 열
            (b['3'] == b['6'] == b['9'] == p) or  # 오른쪽 열
            (b['3'] == b['5'] == b['7'] == p) or  # 대각선
            (b['1'] == b['5'] == b['9'] == p))    # 대각선

def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # 만약에 빈칸이 있다면 False를 반환한다.
    return True  # 빈칸이 없다면 True를 반환한다.


def updateBoard(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark


if __name__ == '__main__':
    main()  # 이 모듈이 임포트되지 않고 실행된다면 main()이 호출된다.
