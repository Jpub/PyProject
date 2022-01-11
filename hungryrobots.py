"""Hungry Robots, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game"""

import random, sys

# 상수 설정하기:
WIDTH = 40           # (!) 이 값을 70 또는 10으로 바꿔 보자.
HEIGHT = 20          # (!) 이 값을 10으로 바꿔 보자.
NUM_ROBOTS = 10      # (!) 이 값을 1 또는 30으로 바꿔 보자.
NUM_TELEPORTS = 2    # (!) 이 값을 0 또는 9999으로 바꿔 보자.
NUM_DEAD_ROBOTS = 2  # (!) 이 값을 0 또는 20으로 바꿔 보자.
NUM_WALLS = 100      # (!) 이 값을 0 또는 300으로 바꿔 보자.

EMPTY_SPACE = ' '    # (!) 이 값을 '.'으로 바꿔 보자.
PLAYER = '@'         # (!) 이 값을 'R'로 바꿔 보자.
ROBOT = 'R'          # (!) 이 값을 '@'로 바꿔 보자.
DEAD_ROBOT = 'X'     # (!) 이 값을 'R'로 바꿔 보자.

# (!) 이 값을 '#'이나, '0', 또는 ' '으로 바꿔 보자:
WALL = chr(9617)  # 문자 9617은 '░'


def main():
    print('''Hungry Robots, by Al Sweigart al@inventwithpython.com

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
'''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # 새로운 게임 셋업:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:  # 메인 게임 루프
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0:  # 플레이어가 이겼는지 확인
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # 플레이어와 로봇을 이동시킴:
        playerPosition = askForPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots:  # 플레이어가 졌는지 확인
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def getNewBoard():
    """보드를 나타내는 딕셔너리를 반환한다.
    키는 보드 위치에 대한 정수 인덱스의 (x, y) 튜플이고,
    값은 WALL, EMPTY_SPACE 또는 DEAD_ROBOT이다.
    또한, 딕셔너리는 플레이어가 순간 이동을 할 수 있는 남은 횟수에 대한 'teleports'라는 키를 가지고 있다.
    살아있는 로봇은 보드 딕셔너리와 분리해서 저장된다."""
    board = {'teleports': NUM_TELEPORTS}

    # 빈 보드 생성하기:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # 보드의 가장자리에 벽 추가하기:
    for x in range(WIDTH):
        board[(x, 0)] = WALL  # 상단 벽 만들기
        board[(x, HEIGHT - 1)] = WALL  # 하단 벽 만들기
    for y in range(HEIGHT):
        board[(0, y)] = WALL  # 왼쪽 벽 만들기
        board[(WIDTH - 1, y)] = WALL  # 오른쪽 벽 만들기

    # 무작위로 벽 추가하기:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # 처음부터 죽어 있는 로봇 추가하기:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """보드의 빈 공간에 대한 (x, y) 정수 튜플을 반환한다."""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """보드에 (x, y)가 비어 있고 거기에 로봇도 없으면
    True를 반환한다."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """보드의 빈 공간에 NUM_ROBOTS개의 로봇을 추가하고
    로봇의 현재 위치인 (x, y) 공간의 리스트를 반환한다."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


def displayBoard(board, robots, playerPosition):
    """보드, 로봇, 그리고 플레이어를 화면에 표시한다."""
    # 보드의 모든 공간에 대해 루프를 돈다:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # 적절한 문자 그리기:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # 개행하기


def askForPlayerMove(board, robots, playerPosition):
    """로봇들의 현재 위치와 보드의 벽이 주어지면
    플레이어가 다음에 이동할 수 있는 장소의 (x, y) 정수 튜플을 반환한다."""
    playerX, playerY = playerPosition

    # 벽으로 막혀 있지 않은 방향을 찾는다:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # 플레이어의 움직임을 얻는다:
        print('(T)eleports remaining: {}'.format(board["teleports"]))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # 플레이어를 임의의 빈 공간으로 텔레포트한다:
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move != '' and move in allMoves:
            # 사용자의 입력에 따라 새로운 위치를 반환한다:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]


def moveRobots(board, robotPositions, playerPosition):
    """플레이어를 향해 이동한 로봇의 새로운 위치에 대한
    (x, y) 튜플 리스트를 반환한다."""
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # 로봇이 움직이는 방향을 결정한다.
        if robotx < playerx:
            movex = 1  # 오른쪽으로 이동
        elif robotx > playerx:
            movex = -1  # 왼쪽으로 이동
        elif robotx == playerx:
            movex = 0  # 수평으로 이동하지 않는다.

        if roboty < playery:
            movey = 1  # 위쪽으로 이동
        elif roboty > playery:
            movey = -1  # 아래쪽으로 이동
        elif roboty == playery:
            movey = 0  # 수직으로 이동하지 않는다.

        # 로봇이 벽에 부딪혔는지 확인하고 코스를 조정한다:
        if board[(robotx + movex, roboty + movey)] == WALL:
            # 로봇이 벽에 부딪혔기 때문에 새로운 움직임을 생각한다:
            if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                movey = 0  # 로봇이 수평 방향으로 움직일 수 없다.
            elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                movex = 0  # 로봇이 수직 방향으로 움직일 수 없다.
            else:
                # 로봇이 움직일 수 없다.
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if (board[(robotx, roboty)] == DEAD_ROBOT
            or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
            # 로봇이 충돌 위치에 있으므로 제거한다.
            del robotPositions[0]
            continue

        # 로봇끼리 부딪혔는지 확인하고, 부딪혔다면 두 로봇 모두 제거한다:
        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx, newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx, newRoboty))
        else:
            nextRobotPositions.append((newRobotx, newRoboty))

        # 로봇이 움직이면 robotPositions에서 로봇을 제거한다.
        del robotPositions[0]
    return nextRobotPositions


# 이 프로그램이 다른 프로그램에 임포트(import)된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
