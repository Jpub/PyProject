"""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com
A stack-moving puzzle game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, game, puzzle"""

import copy
import sys

TOTAL_DISKS = 5  # 더 많은 디스크는 퍼즐의 난이도가 높아진다는 의미다.

# 모든 디스크가 타워 A에 있는 것으로 시작한다:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print("""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    # 타워 설정하기. 리스트의 끝은 타워의 맨 위다.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:  # 한 턴을 실행한다.
        # 타워와 디스크를 표시한다:
        displayTowers(towers)

        # 사용자에게 움직임 요청하기:
        fromTower, toTower = askForPlayerMove(towers)

        # fromTower에서 toTower로 맨 위의 디스크를 옮긴다:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # 사용자가 퍼즐을 풀었는지 확인한다:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)  # 마지막으로 타워를 표시한다.
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True:  # 유효한 움직임을 입력할 때까지 플레이어게 계속 요청한다.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # 사용자가 유효한 타워 문자를 입력했는지 확인한다:
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue  # 플레이어에게 이동을 다시 요청한다.

        # 신택틱 슈거(Syntactic sugar) - 더 짧은 변수명 사용:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # 'from' 타워는 빈 타워일 순 없다:
            print('You selected a tower with no disks.')
            continue  # 플레이어에게 이동을 다시 요청한다.
        elif len(towers[toTower]) == 0:
            # 어떤 디스크도 비어 있는 'to' 타워로 이동할 수 없다:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top of smaller ones.')
            continue  # 플레이어에게 이동을 다시 요청한다.
        else:
            # 유효한 이동이므로, 선택한 타워를 반환한다:
            return fromTower, toTower


def displayTowers(towers):
    """Display the current state."""

    # 세 개의 타워를 표시한다:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)  # 디스크가 없는 기둥 표시한다.
            else:
                displayDisk(tower[level])  # 디스크를 표시한다.
        print()

    # 타워 레이블 A, B, C를 표시한다.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # 디스크 없는 기둥을 표시한다.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # 디스크를 표시한다:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    main()
