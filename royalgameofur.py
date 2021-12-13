"""The Royal Game of Ur, by Al Sweigart al@inventwithpython.com
A 5,000 year old board game from Mesopotamia. Two players knock each
other back as they race for the goal.
More info https://en.wikipedia.org/wiki/Royal_Game_of_Ur
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, board game, game, two-player
"""

import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

# 공간 레이블에 대한 상수 설정하기:
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

#  왼쪽에서 오른쪽으로, 위에서 아래 순서로의 공간:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'  # (H는 집(Home)의 약자, G는 목적지(Goal)의 약자)
O_TRACK = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}           {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {}           {}
"""


def main():
    print('''The Royal Game of Ur, by Al Sweigart

This is a 5,000 year old game. Two players must move their tokens
from their home to their goal. On your turn you flip four coins and can
move one token a number of spaces equal to the heads you got.

Ur is a racing game; the first player to move all seven of their tokens
to their goal wins. To do this, tokens must travel from their home to
their goal:

            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal

If you land on an opponent's token in the middle track, it gets sent
back home. The **flower** spaces let you take another turn. Tokens in
the middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True:  # 메인 게임 루프
        # 이번 턴을 위한 몇 가지 변수들을 설정한다:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME

        displayBoard(gameBoard)

        input('It is ' + turn + '\'s turn. Press Enter to flip...')

        flipTally = 0
        print('Flips: ', end='')
        for i in range(4):  # 4 개의 동전 던지기
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')  # 뒷면
            else:
                print('H', end='')  # 앞면
            if i != 3:
                print('-', end='')  # 구분자 출력하기
            flipTally += result
        print('  ', end='')

        if flipTally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent  # 다른 플레이어에게 턴을 돌린다.
            continue

        # 플레이어에게 이동 요청하기:
        validMoves = getValidMoves(gameBoard, turn, flipTally)

        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent  # 다른 플레이어에게 턴을 돌린다.
            continue

        while True:
            print('Select move', flipTally, 'spaces: ', end='')
            print(' '.join(validMoves) + ' quit')
            move = input('> ').lower()

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in validMoves:
                break  # 유효한 이동이 선택되면 루프를 종료한다.

            print('That is not a valid move.')

        # 선택된 움직임을 보드에서 수행한다:
        if move == 'home':
            # 집에서부터 이동하는 경우라면, 집에서 토큰을 하나 뺀다:
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY  # 기존에 있던 공간을 공백으로 설정한다.
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            # 플레이어가 이겼는지 확인하기:
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            # 상대방이 그 타일에 있는지 확인하기:
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1

            # 도착할 공간을 플레이어의 토큰으로 설정하기:
            gameBoard[nextBoardSpace] = turn

        # 플레이어가 꽃 모양의 공간에 도착하여 한 번 더 이동할 수 있는지 확인한다:
        if nextBoardSpace in FLOWER_SPACES:
            print(turn, 'landed on a flower space and goes again.')
            input('Press Enter to continue...')
        else:
            turn = opponent  # 다른 플레이어에게 턴을 돌린다.

def getNewBoard():
    """
    Returns a dictionary that represents the state of the board. The
    keys are strings of the space labels, the values are X_PLAYER,
    O_PLAYER, or EMPTY. There are also counters for how many tokens are
    at the home and goal of both players.
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # 게임을 시작하기 위해 각 공간을 비운다:
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY
    return board


def displayBoard(board):
    """Display the board on the screen."""
    # 줄바꿈을 많이 출력하여 화면을 깨끗이 정리해,
    # 이전의 보드가 더 이상 보이지 않게 한다.
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7, '.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7, '.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7, '.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7, '.')

    # BOARD_TEMPLATE를 채워야 하는 문자열을
    # 왼쪽에서 오른쪽, 위에서 아래 순서대로 추가한다.
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)
    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])
    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)

    print(BOARD_TEMPLATE.format(*spaces))


def getValidMoves(board, player, flipTally):
    validMoves = []  # 토큰이 이동할 수 있는 공간을 담는다.
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    # 플레이어가 집에서 토큰을 이동할 수 있는지 확인하기:
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('home')

    # 플레이어가 이동할 수 있는 토큰이 있는 공간을 확인하기:
    for trackSpaceIndex, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue
        nextTrackSpaceIndex = trackSpaceIndex + flipTally
        if nextTrackSpaceIndex >= len(track):
            # 목적지까지의 이동 거리 이상이 나와야 한다.
            # 그렇지 않으면 목적지로 이동할 수 없다.
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'G':
                # 이 토큰을 보드 밖으로 빼낼 수 있다.
                validMoves.append(space)
                continue
        if board[nextBoardSpaceKey] in (EMPTY, opponent):
            # 다음으로 이동한 공간이 보호된 중앙 공간이라면,
            # 그곳이 비어 있는 경우에만 해당 공간으로 이동할 수 있다:
            if nextBoardSpaceKey == 'l' and board['l'] == opponent:
                continue  # 이번의 이동을 건너뛰면 그 공간은 보호된다.
            validMoves.append(space)

    return validMoves


if __name__ == '__main__':
    main()
