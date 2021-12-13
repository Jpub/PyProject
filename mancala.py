"""Mancala, by Al Sweigart al@inventwithpython.com
The ancient seed-sowing game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, board game, game, two-player"""

import sys

# 플레이어의 구멍에 대한 튜플:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

# 키가 구멍 이름이고 값이 반대편 구멍 이름인 딕셔너리:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                   'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                   'K': 'E', 'L': 'F'}

# 키가 구멍 이름이고 값이 다음 순서의 구멍 이름인 딕셔너리:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# A부터 시작하여 시계 반대 방향으로 붙여지는 모든 구멍의 레이블:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# 새 게임을 시작할 때 각 구멍에 있게 될 씨앗:
STARTING_NUMBER_OF_SEEDS = 4  # (!) 이 값을 1 또는 10으로 바꿔 보자.


def main():
    print('''Mancala, by Al Sweigart al@inventwithpython.com

The ancient two-player, seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into your store. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    playerTurn = '1'  # 플레이어 1이 먼저 시작한다.

    while True:  # 플레이어의 턴을 실행한다.
        # 여러 개의 줄바꿈을 출력하여 화면을 '깨끗하게' 한다.
        # 따라서 이전 단계의 보드는 화면에서 사라진다.
        print('\n' * 60)
        # 보드를 표시하고 플레이어의 움직임을 받는다:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)

        # 플레이어의 이동을 수행한다:
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # 게임이 끝났는지 어떤 플레이어가 이겼는지 확인한다:
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)  # 최종적으로 보드를 표시한다.
            print('Player ' + winner + ' has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)  # 최종적으로 보드를 표시한다.
            print('There is a tie!')
            sys.exit()


def getNewBoard():
    """Return a dictionary representing a Mancala board in the starting
    state: 4 seeds in each pit and 0 in the stores."""

    # 신택틱 슈거(Syntactic sugar) - 더 짧은 변수명 사용:
    s = STARTING_NUMBER_OF_SEEDS

    # 저장소에 0개의 씨앗이 있고 각 구멍에 초깃값으로 지정된 수의 씨앗이 있는
    # 보드에 대한 데이터 구조를 생성한다:
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def displayBoard(board):
    """Displays the game board as ASCII-art based on the board
    dictionary."""

    seedAmounts = []
    # 이 'GHIJKL21ABCDEF' 문자열은
    # 왼쪽에서 오른쪽으로, 그리고 위에서 아래 순서다:
    for pit in 'GHIJKL21ABCDEF':
        numSeedsInThisPit = str(board[pit]).rjust(2)
        seedAmounts.append(numSeedsInThisPit)

    print("""
+------+------+--<<<<<-Player 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+

""".format(*seedAmounts))


def askForPlayerMove(playerTurn, board):
    """Asks the player which pit on their side of the board they
    select to sow seeds from. Returns the uppercase letter label of the
    selected pit as a string."""

    while True:  # 유효한 입력을 할 때까지 계속 플레이어게 묻는다.
        # 플레이어 쪽 구멍을 선택하도록 요청한다:
        if playerTurn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif playerTurn == '2':
            print('Player 2, choose move: G-L (or QUIT)')
        response = input('> ').upper().strip()

        # 플레이어가 종료하기 원하는지 확인한다:
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 선택할 수 있는 유효한 구멍인지 확인한다:
        if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
            playerTurn == '2' and response not in PLAYER_2_PITS
        ):
            print('Please pick a letter on your side of the board.')
            continue  # 플레이어에게 다시 입력하라고 요청한다.
        if board.get(response) == 0:
            print('Please pick a non-empty pit.')
            continue  # 플레이어에게 다시 입력하라고 요청한다.
        return response


def makeMove(board, playerTurn, pit):
    """Modify the board data structure so that the player 1 or 2 in
    turn selected pit as their pit to sow seeds from. Returns either
    '1' or '2' for whose turn it is next."""

    seedsToSow = board[pit]  # 선택된 구멍에서 씨앗의 수를 가져온다.
    board[pit] = 0  # 선택된 구멍을 비운다.

    while seedsToSow > 0:  # 더 이상 씨앗이 없을 때까지 계속 뿌린다.
        pit = NEXT_PIT[pit]  # 다음 구멍으로 이동한다.
        if (playerTurn == '1' and pit == '2') or (
            playerTurn == '2' and pit == '1'
        ):
            continue  # 상대방의 저장소는 건너뛴다.
        board[pit] += 1
        seedsToSow -= 1

    # 마지막 씨앗이 플레이어의 저장소에 들어간다면, 다시 턴을 얻는다.
    if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
        # 마지막 씨앗이 플레이어의 저장소에 도착했다. 다시 턴을 얻는다.
        return playerTurn

    # 마지막 씨앗이 빈 구멍에 도착했는지 확인한다. 그렇다면 반대편 구멍에 있는 씨앗을 가져온다.
    if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['1'] += board[oppositePit]
        board[oppositePit] = 0
    elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        oppositePit = OPPOSITE_PIT[pit]
        board['2'] += board[oppositePit]
        board[oppositePit] = 0

    # 다음 플레이어로 반환한다:
    if playerTurn == '1':
        return '2'
    elif playerTurn == '2':
        return '1'


def checkForWinner(board):
    """Looks at board and returns either '1' or '2' if there is a
    winner or 'tie' or 'no winner' if there isn't. The game ends when a
    player's pits are all empty; the other player claims the remaining
    seeds for their store. The winner is whoever has the most seeds."""

    player1Total = board['A'] + board['B'] + board['C']
    player1Total += board['D'] + board['E'] + board['F']
    player2Total = board['G'] + board['H'] + board['I']
    player2Total += board['J'] + board['K'] + board['L']

    if player1Total == 0:
        # 플레이어 2는 자기 쪽에 남아 있는 모든 씨앗을 가져온다:
        board['2'] += player2Total
        for pit in PLAYER_2_PITS:
            board[pit] = 0  # 모든 구멍을 0으로 설정한다.
    elif player2Total == 0:
        # 플레이어 1은 자기 쪽에 남아 있는 모든 씨앗을 가져온다:
        board['1'] += player1Total
        for pit in PLAYER_1_PITS:
            board[pit] = 0  # 모든 구멍을 0으로 설정한다.
    else:
        return 'no winner'  # 승자가 아직 없다.

    # 게임 종료. 점수가 가장 높은 플레이어를 찾는다.
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
