"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# 상수 설정:
WIDTH, HEIGHT = bext.size()
# 줄바꿈을 자동으로 추가하지 않으면 윈도우즈의 마지막 열에 출력할 수 없으므로,
# 넓이를 1 줄인다:
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (!) 이것을 1 또는 100으로 변경해 보자.
PAUSE_AMOUNT = 0.2  # (!) 이것을 1.0 또는 0.0으로 변경해 보자.
# (!) 이 리스트가 더 적은 색상을 가지도록 변경해 보자:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# logo 딕셔너리에 대한 키 이름:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # 몇 개의 로고 생성하기
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # X가 짝수여야 코너에 닿을 수 있기 때문에 짝수가 되도록 한다.
            logos[-1][X] -= 1

    cornerBounces = 0  # 로고가 코너에 닿은 횟수.
    while True:  # 메인 프로그램 루프
        for logo in logos:  # logos 리스트에 있는 각 logo에 대한 처리.
            # logo의 현재 위치 지우기:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')  # (!) 이 코드를 주석 처리해 보자.

            originalDirection = logo[DIR]

            # logo가 코너에 닿았는지 확인:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # logo가 왼쪽 끝에 닿았는지 확인:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # logo가 오른쪽 끝에 닿았는지 확인:
            # (WIDTH - 3해야 한다. 왜냐하면 'DVD'는 3개의 문자로 되어 있기 때문이다.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # logo가 상단 끝에 닿았는지 확인:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # logo가 하단 끝에 닿았는지 확인:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # 로고가 튕겨 나올 때 색상을 바꾼다:
                logo[COLOR] = random.choice(COLORS)

            # 로고를 이동시킴
            # (터미널의 문자가 두 배 크기 때문에 X를 2씩 이동한다.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # 코너에 닿은 횟수를 표시:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # 새로운 위치에 로고를 그린다:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # (bext를 사용하는 프로그램에 필요한 부분)
        time.sleep(PAUSE_AMOUNT)


# 이 프로그램이 다른 프로그램에 임포트된 게 아니라면 게임이 실행된다:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # Ctrl-C를 누르면 게임이 종료된다.
