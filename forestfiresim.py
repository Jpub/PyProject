"""Forest Fire Sim, by Al Sweigart al@inventwithpython.com
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정하기:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) 이들 설정을 0.0에서 1.0 사이의 값으로 바꿔 보자:
INITIAL_TREE_DENSITY = 0.20  # 초기에 시작하는 나무의 양
GROW_CHANCE = 0.01  # 빈 공간이 나무로 될 확률
FIRE_CHANCE = 0.01  # 나무가 번개에 맞아 타버릴 확률

# (!) 일시 중지 길이를 1.0 또는 0.0으로 바꿔 보자:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # 메인 게임 루프
        displayForest(forest)

        # 단일 시뮬레이션 단계 실행하기:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # 이전의 반복문에서 nextForest[(x, y)]를 이미 설정했다면
                    # 여기서는 아무런 작업을 하지 않는다:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # 여기의 빈 공간에 나무가 자란다.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # 번개가 나무에 불을 붙인다.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # 이 나무는 현재 타고 있다.
                    # 주변 공간 모두에 대해 루프를 돈다:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # 인접 나무에 불이 옮는다:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # 나무가 다 탔기 때문에 제거한다:
                    nextForest[(x, y)] = EMPTY
                else:
                    # 기존의 상태를 그대로 복사한다:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # 나무로 시작한다.
            else:
                forest[(x, y)] = EMPTY  # 빈 공간으로 시작한다.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # 디폴트 폰트 색상을 사용한다.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
