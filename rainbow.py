"""Rainbow, by Al Sweigart al@inventwithpython.com
Shows a simple rainbow animation. Press Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic, bext, beginner, scrolling"""

import time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0  # 들어쓰기할 공백 개수
indentIncreasing = True  # 들어쓰기가 증가하는지 아닌지 여부

try:
    while True:  # 메인 프로그램 루프
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            # 공백 개수를 증가시킨다:
            indent = indent + 1
            if indent == 60:  # (!) 이 값을 10 또는 30으로 바꿔 보자.
                # 방향 전환:
                indentIncreasing = False
        else:
            # 공백 개수를 감소시킨다:
            indent = indent - 1
            if indent == 0:
                # 방향 전환:
                indentIncreasing = True

        time.sleep(0.02)  # 잠깐 멈춤 추가
except KeyboardInterrupt:
    sys.exit()  # Ctrl-C를 누르면 프로그램을 종료한다.
